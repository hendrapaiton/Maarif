from django.urls import path
from portal.views import LoginView, ProtectedEndpointView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('protected-endpoint/', ProtectedEndpointView.as_view(), name='protected-endpoint'),
]
