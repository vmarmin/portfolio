from django import forms
from .models import Post, Comment
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name="post"))

    class Meta:
        model = Post
        fields = (
            "title",
            "overview",
            "content",
            "thumbnail",
            "categories",
            "featured",
            "previous_post",
            "next_post",
        )


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorWidget(config_name="comment"), placeholder="Type your comment"
    )

    class Meta:
        model = Comment
        fields = ("content",)
