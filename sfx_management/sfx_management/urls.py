# sfx_management/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('upload/', views.upload_sound_effect, name='upload_sound_effect'),
    path('success/<int:sound_effect_id>/', views.success, name='success'),
    path('list_files/', views.list_files, name='list_files'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   
   









   
   









