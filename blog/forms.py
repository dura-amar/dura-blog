from django import forms
from  blog.models import BlogPost,Category

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=['title','content','category','thumbnail']

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']