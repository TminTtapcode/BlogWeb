from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Dựa trên Model 'Post'
        fields = ['title', 'content'] # Chỉ hiển thị 2 trường này