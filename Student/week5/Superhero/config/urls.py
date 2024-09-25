from django.contrib import admin
from django.urls import path
from hero.views import HeroDetailView, HeroListView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', HeroListView.as_view(), name='hero_list'),
    path('hero/<str:name>', HeroDetailView.as_view(), name = 'hero_detail'),
]