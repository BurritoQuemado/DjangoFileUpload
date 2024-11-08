
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.core.cache import cache
import logging
from .serializers import UploadSerializer

logger = logging.getLogger(__name__)

class FileUploadView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            try:
                file_instance = serializer.save()

                cache.set(f'file_{file_instance.id}',{
                    'file_url': file_instance.file.url,
                    'uploaded_at': file_instance.uploaded_at,
                    'user_id': request.user.id
                }, timeout=86400) #cache for 1 day

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error(f'File upload failed {str(e)}')
                return Response({"error": "File upload failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
