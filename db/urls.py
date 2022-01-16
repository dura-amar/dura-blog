"""db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from authentication.views import view_user_register

from blog.views import view_aBlog, view_aBlog_bySlug, view_aCategory, view_aCategory_byName, view_add_aBlog, view_add_aCategory, view_add_comment, view_allBlogs, view_allCategory, view_delete_blog, view_update_blog, view_search_blog_title,view_my_blogs
from home.views import view_about_me, view_fb, view_gh, view_ig, view_ln, view_tw

urlpatterns = [
    path('admin/', admin.site.urls),

    path('blogs/category/', view_allCategory, name='view_allCategory'),
    path('blogs/category/<int:cId>', view_aCategory, name='view_aCategory'),
    path('blogs/category/<str:categoryName>', view_aCategory_byName, name='view_aCategory_byName'),
    path('blogs/category/new/add', view_add_aCategory, name='add_aCategory'),
    
    path('blogs/', view_allBlogs, name='view_allBlogs'),
    path('blogs/i/<int:blog_id>', view_aBlog, name='view_aBlog'),
    path('blogs/s/<slug:blog_slug>', view_aBlog_bySlug, name='view_aBlog_bySlug'),
    path('blogs/add', view_add_aBlog, name='add_aBlog'),

    # update a blog
    path('blogs/update/<slug:blog_slug>', view_update_blog, name='update_aBlog'),
    # delete a blog
    path('blogs/delete/<int:blog_id>', view_delete_blog, name='delete_aBlog'),

    #for logout, login, register
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', view_user_register, name='register'),


    # for search functionality
    path('search-blog/', view_search_blog_title, name='search_blog_title'),

    # for blogs published by me
    path('my-blogs/', view_my_blogs, name='my_blogs'),
   
]

new_urlpatterns = [
    # for comments
    path('blogs/comment/<int:blog_id>', view_add_comment, name='add_comment'),

    #for about page
    path('about/', view_about_me, name='about_me'),


    # for social media links
    path('fb/', view_fb, name='fb'),
    path('ig/', view_ig, name='ig'),
    path('ln/', view_ln, name='ln'),
    path('tw/', view_tw, name='tw'),
    path('gh/', view_gh, name='gh'),
]

urlpatterns +=new_urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
