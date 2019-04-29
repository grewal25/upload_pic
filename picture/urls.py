from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='picture'

urlpatterns = [
    path('image_upload', views.hotel_image_view, name = 'image_upload'),
    path('success', views.success, name = 'success'),
    path('',views.index, name='index'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
