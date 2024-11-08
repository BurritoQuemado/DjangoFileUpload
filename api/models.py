from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'

class Upload(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    uploaded_timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -{self.file.name}"