from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response

from account.models import User
from account.serializers import (
    MyTokenObtainPairSerializer,
    UserSignUpSerializer,
    UserUpdateSerializer,
)


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


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer


class UserUpdateDestroyAPIView(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    
    
    def put(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)
    
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)
    
    
