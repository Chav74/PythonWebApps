from django.contrib import admin
from django.urls import path
from hero.views import HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add/',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete/', HeroDeleteView.as_view(),  name='hero_delete'),
    path('edit/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('add/', HeroCreateView.as_view(),  name='add'),
    path('<int:pk>/',        HeroDetailView.as_view(),  name='hero_detail'),
    path('delete/',           HeroDeleteView.as_view(),  name='hero_delete'),
]