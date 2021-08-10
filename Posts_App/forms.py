from django import forms
from Posts_App.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'caption', 'private', 'public']