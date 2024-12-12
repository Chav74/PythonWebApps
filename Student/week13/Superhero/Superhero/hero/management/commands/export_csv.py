import csv
from django.core.management.base import BaseCommand
from hero.models import Superhero, Article

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('superheroes.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'identity', 'description', 'image', 'strengths', 'weaknesses'])  
            for hero in Superhero.objects.all():
                writer.writerow([hero.name, hero.identity, hero.description, hero.image, hero.strengths, hero.weaknesses])

        with open('articles.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['title', 'body', 'author_id'])  
            for article in Article.objects.all():
                writer.writerow([article.title, article.body, article.author_id])