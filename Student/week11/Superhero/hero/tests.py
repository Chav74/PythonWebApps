from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from hero.models import Investigator, Superhero, Article

def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')

def test_user():
    return get_user_model().objects.create_user(**user_args())

# Superhero Data and View Tests
class SuperheroDataTest(TestCase):
    def setUp(self):
        self.user = test_user()
        self.hero1 = dict(name='NAME 1', identity="ID 1")
        self.hero2 = dict(name='NAME 2', identity="ID 2")

    def test_add(self):
        self.assertEqual(Superhero.objects.count(), 0)
        Superhero.objects.create(**self.hero1)
        x = Superhero.objects.get(pk=1)
        self.assertEqual(x.name, self.hero1['name'])
        self.assertEqual(Superhero.objects.count(), 1)

    def test_edit(self):
        superhero = Superhero.objects.create(**self.hero1)
        superhero.name = self.hero2['name']
        superhero.identity = self.hero2['identity']
        superhero.save()
        self.assertEqual(superhero.name, self.hero2['name'])
        self.assertEqual(superhero.identity, self.hero2['identity'])
        self.assertEqual(Superhero.objects.count(), 1)

    def test_delete(self):
        superhero = Superhero.objects.create(**self.hero1)
        superhero.delete()
        self.assertEqual(Superhero.objects.count(), 0)

class SuperheroViewsTest(TestCase):
    def login(self):
        response = self.client.login(username=self.user.username, password=user_args()['password'])
        self.assertTrue(response)

    def setUp(self):
        self.user = test_user()
        self.hero1 = dict(name='NAME 1', identity="ID 1")
        self.hero2 = dict(name='NAME 2', identity="ID 2")

    def test_home(self):
        response = self.client.get(reverse('hero_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/list.html')
        self.assertContains(response, 'Superhero List') 

    def test_hero_list_view(self):
        Superhero.objects.create(**self.hero1)
        Superhero.objects.create(**self.hero2)
        response = self.client.get(reverse('hero_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=3)  

    def test_hero_detail_view(self):
        Superhero.objects.create(**self.hero1)
        response = self.client.get(reverse('hero_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.hero1['name'])

    def test_hero_edit_view(self):
        superhero = Superhero.objects.create(**self.hero1)
        response = self.client.get(reverse('hero_edit', args=[superhero.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/edit.html')

    def test_hero_delete_view(self):
        superhero = Superhero.objects.create(**self.hero1)
        response = self.client.get(reverse('hero_delete', args=[superhero.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hero/delete.html')

# Investigator Tests
class InvestigatorDataTest(TestCase):
    def setUp(self):
        self.user = test_user()
        self.investigator_data = dict(name="Investigator Name")

    def test_create_investigator(self):
        investigator = Investigator.objects.create(**self.investigator_data)
        self.assertEqual(investigator.name, "Investigator Name")

class InvestigatorViewsTest(TestCase):
    def setUp(self):
        self.user = test_user()
        self.investigator = Investigator.objects.create(name="Investigator Name")

    def test_investigator_list_view(self):
        response = self.client.get(reverse('investigator_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'investigator/list.html')
        self.assertContains(response, 'Investigator Name')  

# Article Data Tests
class ArticleDataTest(TestCase):
    def setUp(self):
        self.user = test_user()
        self.article_data = dict(title="Article Title", markdown="*Body*", author=self.user)
        self.article = Article.objects.create(**self.article_data)

    def test_create_article(self):
        self.assertEqual(self.article.title, "Article Title")
        self.assertEqual(self.article.markdown, "*Body*")
        self.assertEqual(self.article.author, self.user)
        self.assertIn("<em>Body</em>", self.article.html)  

    def test_article_detail_view(self):
        response = self.client.get(reverse('article_detail', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/detail.html')
        self.assertContains(response, self.article.title)
