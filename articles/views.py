from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article
# Create your views here.

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article/list.html'
    context_object_name = 'articles'
    
    
    
class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article 
    template_name = 'article/detail.html'
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article/new.html'
    fields = ['title','body']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article 
    template_name = 'article/edit.html'
    fields = ['title','body']
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    
class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article 
    template_name = 'article/delete.html'
    success_url = reverse_lazy('list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

