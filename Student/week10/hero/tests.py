from django.test import TestCase
from hero.models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.article = Article.objects.create(title='Test Article', body='Content', author=self.user)

    def test_article_author_edit_permission(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(f'/articles/{self.article.id}/edit/')
        self.assertEqual(response.status_code, 200)

       
        other_user = User.objects.create_user(username='otheruser', password='password')
        self.client.login(username='otheruser', password='password')
        response = self.client.get(f'/articles/{self.article.id}/edit/')
        self.assertNotEqual(response.status_code, 200)