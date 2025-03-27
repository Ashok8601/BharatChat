from django.db import models

# Create your models here.
class Chat(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)  # For text message
    media = models.FileField(upload_to='chat_media/', blank=True, null=True)  # For image/video/pdf/audio
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.receiver}'
