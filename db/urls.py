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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import view_aBlog, view_aCategory, view_add_aBlog, view_add_aCategory, view_allBlogs, view_allCategory

urlpatterns = [
    path('admin/', admin.site.urls),

    path('category/', view_allCategory, name='view_allCategory'),
    path('category/<int:cId>', view_aCategory, name='view_aCategory'),
    path('category/add', view_add_aCategory, name='add_aCategory'),

    path('blogs/',view_allBlogs, name='view_allBlogs'),
    path('blogs/<int:bId>',view_aBlog,name='view_aBlog'),
    path('blogs/add',view_add_aBlog,name='add_aBlog'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)