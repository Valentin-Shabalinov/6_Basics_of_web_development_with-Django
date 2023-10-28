from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.text import slugify

from post.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'image', 'date_of_creation', 'publication_sign')
    success_urt = reverse_lazy('post:list')
    extra_context = {
        'title': "Создание записи"
    }

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)
    

class PostListView(ListView):
    model = Post
    extra_context = {
        'title': 'Записи'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset (*args, **kwargs)
        queryset = queryset. filter(publication_sign=True)
        return queryset

class PostDetailView(DetailView):
    model = Post
    extra_context = {
        'title': 'Просмотр записи'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object. count_views += 1
        self.object.save()

        return self.object
    
class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('post:list')
    extra_context = {
        'title': 'Редактирование записи'
    }

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


    def get_success_url(self) -> str:
        return reverse('post:view', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post:list')
    extra_context = {
        'title': 'Удаление записи'
    }

