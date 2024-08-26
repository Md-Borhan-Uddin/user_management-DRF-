from rest_framework.views import APIView

from rest_framework.response import Response

from account.models import User
from account.serializers import MyTokenObtainPairSerializer, UserSignUpSerializer

from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),  # type: ignore
    }


class UserSignUpAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = MyTokenObtainPairSerializer.get_token(user)
        return Response(
            {
                "refresh": str(token),
                "access": str(token.access_token),  # type: ignore
            }
        )
