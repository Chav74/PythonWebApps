from django.contrib import admin
from django.urls import path, include
from hero.views import (
    HeroListView, HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView,
    InvestigatorListView, InvestigatorDetailView, InvestigatorCreateView, InvestigatorUpdateView, InvestigatorDeleteView,
    ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView,
)
from django.contrib.auth.views import LoginView

from hero.views_accounts import UserAddView, UserUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls), 
    path('', HeroListView.as_view(), name='hero_list'),
    path('hero/<int:pk>/', HeroDetailView.as_view(), name='hero_detail'),
    path('hero/add/', HeroCreateView.as_view(), name='hero_add'),
    path('hero/<int:pk>/edit/', HeroUpdateView.as_view(), name='hero_edit'),
    path('hero/<int:pk>/delete/', HeroDeleteView.as_view(), name='hero_delete'),

 
    path('investigator/', InvestigatorListView.as_view(), name='investigator_list'),
    path('investigator/<int:pk>/', InvestigatorDetailView.as_view(), name='investigator_detail'),
    path('investigator/add/', InvestigatorCreateView.as_view(), name='investigator_add'),
    path('investigator/<int:pk>/edit/', InvestigatorUpdateView.as_view(), name='investigator_edit'),
    path('investigator/<int:pk>/delete/', InvestigatorDeleteView.as_view(), name='investigator_delete'),

   
    path("article/", ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("article/add/", ArticleCreateView.as_view(), name="article_add"),
    path("article/<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("article/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),

    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', UserAddView.as_view(), name='signup'),
    path('accounts/<int:pk>/', UserUpdateView.as_view(), name='account_edit'),


     path('', include('photos.urls')),
]