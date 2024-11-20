from django.core.management.base import BaseCommand
from json import loads
from pathlib import Path

from hero.models import Superhero, Article


def load_data():
    # Delete the old objects
    Superhero.objects.all().delete()
    Article.objects.all().delete()  # Delete Article objects as well

    # Read the JSON file
    path = Path('hero_objects.json')
    if path.exists():
        with open(path, 'r') as f:
            data = loads(f.read())  # Use loads to parse JSON data

        # Create Superhero objects
        for superhero_data in data.get('superheroes', []):  # Handle missing key
            Superhero.objects.get_or_create(**superhero_data)

        # Create Article objects
        for article_data in data.get('articles', []):  # Handle missing key
            Article.objects.get_or_create(**article_data)

    # Show the objects 
    for hero in Superhero.objects.all().values():
        print(hero)

    for article in Article.objects.all().values():
        print(article)