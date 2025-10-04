from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='services'),
    path('seo/', views.seo, name='seo'),
    path('ppc/', views.ppc, name='ppc'),
    path('website-development/', views.website_development, name='website_development'),
    path('apps/', views.apps, name='apps'),
    path('video-marketing/', views.video_marketing, name='video_marketing'),
]