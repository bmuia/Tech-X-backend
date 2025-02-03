from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register')
]