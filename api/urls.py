from django.urls import path
from .views import FileUploadView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token endpoint
]
