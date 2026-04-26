from django import forms
from .models import Post

class PostForm(forms.ModelForm): #class for settings 
    class Meta:
        model = Post
        fields = ["title", "body", "author", "is_published"]
