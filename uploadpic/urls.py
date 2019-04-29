"""uploadpic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please s
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('picture/', include('picture.urls'), name='picture'),
]
