from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm): #class for settings 
    class Meta:
        model = Post
        fields = ["title", "body", "author", "is_published"]

class CommentForm(forms.ModelForm): #class for settings 
    class Meta:
        model = Comment
        fields = ["author", "txt"]
