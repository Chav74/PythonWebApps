import csv
from django.core.management.base import BaseCommand
from hero.models import Superhero, Article
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('superheroes.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  
            for row in reader:
                Superhero.objects.get_or_create(name=row[0], identity=row[1], description=row[2], image=row[3], strengths=row[4], weaknesses=row[5])

        with open('articles.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) 
            for row in reader:
                author_id = row[2]
                try:
                    author = get_user_model().objects.get(pk=author_id)
                except get_user_model().DoesNotExist:
                    author = None  
                Article.objects.get_or_create(title=row[0], body=row[1], author=author)