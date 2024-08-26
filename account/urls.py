from django.urls import path

from account.views import UserListCreateAPIView, UserSignUpAPIView


urlpatterns = [
    path("sign-up", UserSignUpAPIView.as_view(), name='user_signup'),
    path("users/", UserListCreateAPIView.as_view(), name="users")
]
