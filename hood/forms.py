from django import forms
from .models import Profile,BlogPost,Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        exclude=['username','neighbourhood','avatar']


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']
