from rest_framework import serializers
from .models import Upload
import magic

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['id', 'file', 'uploaded_at', 'user']

    def validate_file(self, value):

        # Limit file size to 10 GB
        max_size = 10240 * 1024 * 1024  # 10 GB
        # Min file size to 1 GB
        min_size = 1024 * 1024 * 1024 # 1 GB

        if value.size > max_size:
            raise serializers.ValidationError("File size too large. Max size is 7 GB.")
        
        if value.size < min_size:
            raise serializers.ValidationError("File size too small. Min size is 1 GB.")
        
        # Validate allowed file types
        mime_type = magic.from_buffer(value.read(), mime=True)
        allowed_types = ['video/mp4', 'audio/mpeg','audio/ogg', 'video/webm']
        if mime_type not in allowed_types:
            raise serializers.ValidationError("Unsupported file type")
        
        return value
