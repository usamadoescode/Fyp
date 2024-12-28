from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):  # Class names should be capitalized by convention

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='postphoto/', blank=True, null=True)
    restaurant_name = models.CharField(max_length=255,blank=False,null=False)
    restaurant_location= models.CharField(max_length=100,blank=False,null=False)

    restaurant_num =models.IntegerField(blank=True,null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'
