from django import forms
from .models import Review

class User_Review(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text','image','restaurant_name','restaurant_location','restaurant_num']