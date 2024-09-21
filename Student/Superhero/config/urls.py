
from django.urls import path
from hero.views import HeroListView, HulkView,IronManView, BlackWidowView, SpiderManView, CaptainAmericaView


urlpatterns = [
    path('', HeroListView.as_view()),
    path('hero/Hulk/', HulkView.as_view()),
    path('hero/Iron Man/', IronManView.as_view()),
    path('hero/Black Widow/', BlackWidowView.as_view()),
    path('hero/Spider-Man/', SpiderManView.as_view()),
    path('hero/Captain America/', CaptainAmericaView.as_view()),
    

]
