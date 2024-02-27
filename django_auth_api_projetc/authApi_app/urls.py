from django.urls import path
from .views import UserRegistrationView, UserLoginView, ProfileDetailsView, UserChangePasswordView

urlpatterns = [

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('userprofile/', ProfileDetailsView.as_view(), name='userprofile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
]
