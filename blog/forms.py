from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'body': forms.Textarea(attrs={'placeholder': 'Your Comment'}),
        }