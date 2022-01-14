from django import forms
from  blog.models import BlogPost,Category
from crispy_forms.helper import FormHelper

class BlogPostForm(forms.ModelForm):
    helper =FormHelper()
    class Meta:
        model=BlogPost
        fields=['title','content','category','author','thumbnail']

class CategoryForm(forms.ModelForm):
    helper =FormHelper()
    class Meta:
        model=Category
        fields=['name']