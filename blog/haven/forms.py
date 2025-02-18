from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Comment, Article


class CreateuserForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'description', 'categorys', 'content']
