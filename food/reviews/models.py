from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):  # Class names should be capitalized by convention

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='postphoto/', blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'
