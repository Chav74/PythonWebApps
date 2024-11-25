from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article,Investigator

from .models import Superhero

class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero
    context_object_name = 'heroes'

class HeroDetailView(DetailView):
    model = Superhero
    template_name = 'hero/hero.html'
    context_object_name = 'hero'
    

class HeroCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user

class HeroUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'

    def test_func(self):
        superhero = self.get_object()
        return self.request.user.is_superuser or self.request.user

class HeroDeleteView(LoginRequiredMixin,DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url=reverse_lazy('hero_list')

class ArticleListView(ListView):
    template_name = 'article/list.html'
    model = Article
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    template_name = 'article/detail.html'
    model = Article
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article/add.html'
    model = Article
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'article/edit.html'
    model = Article
    fields = '__all__'

    def test_func(self):
        return self.get_object().author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article/delete.html'
    success_url = reverse_lazy("article_list")

    def test_func(self):
        return self.get_object().author == self.request.user
    


class InvestigatorListView(ListView):
    template_name = 'investigator/list.html'
    model = Investigator
    context_object_name = 'investigators'

class InvestigatorDetailView(DetailView):
    template_name = 'investigator/detail.html'
    model = Investigator
    context_object_name = 'investigator'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        investigator = self.get_object()
        context['articles'] = Article.objects.filter(author=investigator.user)
        return context

class InvestigatorCreateView(LoginRequiredMixin, CreateView):
    template_name = 'investigator/add.html'
    model = Investigator
    fields = '__all__'

class InvestigatorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'investigator/edit.html'
    model = Investigator
    fields = '__all__'

class InvestigatorDeleteView(LoginRequiredMixin, DeleteView):
    model = Investigator
    template_name = 'investigator/delete.html'
    success_url = reverse_lazy('investigator_list')