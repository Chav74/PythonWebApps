from json import loads
from json import dump
from django.core.management.base import BaseCommand

from hero.models import Superhero, Article  # Import Article model

class Command(BaseCommand):
    def handle(self, *args, **options):
        save_data()

def save_data():
    data = {
        "superheroes": list(Superhero.objects.all().values()),
        "articles": list(Article.objects.all().values())  # Include articles
    }

    with open('hero_objects.json', "w") as f:
        dump(data, f, indent=4) 