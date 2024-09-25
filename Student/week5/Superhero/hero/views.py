from django.views.generic import ListView, DetailView
from .models import Superhero

class HeroListView(ListView):
    model=Superhero
    template_name = 'index.html'

    

class HeroDetailView(DetailView):
    model =Superhero
    template_name = 'hero.html'

    def get_object(self):
        return Superhero.objects.get(name=self.kwargs['name'])