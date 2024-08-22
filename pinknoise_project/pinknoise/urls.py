# pinknoise/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('dsp/', views.dsp_view, name='dsp_view'),
# ]

# pinknoise_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dsp_view, name='dsp_view'),
]




