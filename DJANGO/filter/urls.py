from django.urls import path

from . import views

app_name = "filter"
urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.apply, name='apply'),
    path('apply/grayscale/', views.grayscale, name='grayscale'),
    path('apply/sepia/', views.sepia, name='sepia'),
    path('apply/inversion/', views.inversion, name='inversion'),
    path('apply/sketch', views.sketch, name='sketch'),
    path('apply/mirror_relection/', views.mirror_reflection, name='mirror_reflection'),
    path('apply/water_reflection/', views.water_reflection, name='water_reflection'),
    path('apply/rotate_left/', views.rotate_left, name='rotate_left'),
    path('apply/rotate_right/', views.rotate_right, name='rotate_right'),
    path('apply/blur/', views.blur, name='blur'),
    path('apply/edge/', views.edge, name='edge'),
    path('apply/home/', views.home, name='home'),
    path('apply/save/', views.save, name='save'),
    path('apply/download/', views.download, name='download'),
]
