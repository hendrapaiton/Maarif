from django.urls import path
from portal.views import ProtectedEndpointView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='access_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/protected-endpoint/', ProtectedEndpointView.as_view(), name='protected-endpoint'),
]
