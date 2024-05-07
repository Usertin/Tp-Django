from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
# Create your views here.
class ListePosts(ListView):
    model = Post
    template_name = 'liste_posts.html'
    context_object_name = 'posts'

class DetailPost(DetailView):
    model = Post
    template_name = 'detail_post.html'
    context_object_name = 'post'


class CreerPost(CreateView):
    model = Post
    template_name = 'creer_post.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_posts')
    #obtenir la liste des argument pour la form, ceci est utilisé pour obtenir l'utilisateur courant
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ModifierPost(UpdateView):
    model = Post
    template_name = 'modifier_post.html'
    form_class = PostForm
    success_url = reverse_lazy('liste_posts')

class SupprimerPost(DeleteView):
    model = Post
    template_name = 'supprimer_post.html'
    success_url = reverse_lazy('liste_posts') 