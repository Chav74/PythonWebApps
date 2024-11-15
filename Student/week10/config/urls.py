from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from hero.views import HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView
from hero.views_accounts import UserAddView, UserUpdateView
from hero.views import *


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
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/',            UserAddView.as_view(),      name='signup'),
    path('accounts/<int:pk>/', UserUpdateView.as_view(), name='account_edit'),
    path('accounts/profile/', UserUpdateView.as_view(), name='account_edit'),

    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    

    # Article
    path("article/", ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
    path("article/add", ArticleCreateView.as_view(), name="article_add"),
    path("article/<int:pk>/", ArticleUpdateView.as_view(), name="article_edit"),
    path("article/<int:pk>/delete", ArticleDeleteView.as_view(), name="article_delete"),

]