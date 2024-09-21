from pathlib import Path
from django.views.generic import TemplateView


class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        heroes=['Iron Man','Black Widow','Hulk','Spider-Man','Captain America']
        return {'heroes':heroes}
    
class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'id': 'Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }
class IronManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Iron Man',
            'id': 'Tony',
            'image': '/static/images/iron_man.jpg'
        }
class BlackWidowView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Widow',
            'id': 'Natasha',
            'image': '/static/images/black_widow.jpg'
        }
class SpiderManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spider-Man',
            'id': 'Peter',
            'image': '/static/images/spider_man.jpg'
        }
class CaptainAmericaView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Captain America',
            'id': 'Steve',
            'image': '/static/images/captain_america.jpg'
        }