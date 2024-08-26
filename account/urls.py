from django.urls import path

from account.views import UserListCreateAPIView, UserSignUpAPIView, UserUpdateDestroyAPIView


urlpatterns = [
    path("sign-up", UserSignUpAPIView.as_view(), name='user_signup'),
    path("users/", UserListCreateAPIView.as_view(), name="users"),
    path("user/<int:pk>/", UserUpdateDestroyAPIView.as_view(), name="user_update_retrieve"),
]
