from django.contrib import admin

from blog.models import BlogComment, BlogPost, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(BlogComment)


class BlogPostAdmin(admin.ModelAdmin):
    # you should prevent author field to be manipulated 
    readonly_fields = ['author']

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        BlogPost.author = request.user
        return super().get_form(request, obj, **kwargs)


    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
admin.site.register(BlogPost, BlogPostAdmin)