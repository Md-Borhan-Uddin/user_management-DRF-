from django.urls import path

from account.views import UserSignUpAPIView


urlpatterns = [
    path("sign-up", UserSignUpAPIView.as_view(), name='user_signup'),
    
]
