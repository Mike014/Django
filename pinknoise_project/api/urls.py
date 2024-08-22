# pinknoise_project/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import dsp_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', dsp_view, name='dsp_view'),
]
