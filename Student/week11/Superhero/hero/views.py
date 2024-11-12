from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article

from .models import Superhero

class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero
    context_object_name = 'heroes'

class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero
    context_object_name = 'hero'
    

class HeroCreateView(LoginRequiredMixin,CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'

class HeroUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'

class HeroDeleteView(LoginRequiredMixin,DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url=reverse_lazy('hero_list')

class ArticleListView(ListView):
    template_name = "article/list.html"
    model = Article
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    template_name = "article/detail.html"
    model = Article
    context_object_name = "article"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/add.html"
    model = Article
    fields = "__all__"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article/edit.html"
    model = Article
    fields = "__all__"

    def test_func(self):
        return self.get_object().author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "article/delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        return self.get_object().author == self.request.user
