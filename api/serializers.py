from rest_framework import serializers
from .models import Upload
import magic

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['id', 'file', 'uploaded_at', 'user']

    def validate_file(self, value):

        # Limit file size to 7 GB
        max_size = 7168 * 1024 * 1024  # 7 GB
        if value.size > max_size:
            raise serializers.ValidationError("File size too large. Max size is 7 GB.")
        
        # Validate allowed file types
        mime_type = magic.from_buffer(value.read(), mime=True)
        allowed_types = ['video/mp4', 'audio/mpeg','audio/ogg', 'video/webm']
        if mime_type not in allowed_types:
            raise serializers.ValidationError("Unsupported file type")
        
        return value
