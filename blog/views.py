from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .models import *

class NewsList(ListView):
    paginate_by = 2
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'

