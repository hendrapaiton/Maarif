from django.urls import path
from portal.views import CookieTokenObtainPairView, CookieTokenRefreshView, ProtectedEndpointView

urlpatterns = [
    path('api/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected-endpoint/', ProtectedEndpointView.as_view(), name='protected-endpoint'),
]
