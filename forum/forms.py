from django import forms

from .models import ForumPost, ForumComment

class PostForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = ForumComment
        fields = ('text',)
