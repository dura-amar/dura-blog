from django import forms
from  blog.models import BlogComment, BlogPost,Category
from crispy_forms.helper import FormHelper

class BlogPostForm(forms.ModelForm):
    helper =FormHelper()
    class Meta:
        model=BlogPost
        fields=['title','content','category','thumbnail']

class CategoryForm(forms.ModelForm):
    helper =FormHelper()
    class Meta:
        model=Category
        fields=['name']

class BlogCommentForm(forms.ModelForm):
    helper =FormHelper()
    class Meta:
        model=BlogComment
        fields=['comment']