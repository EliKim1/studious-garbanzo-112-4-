from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.url import reverse_lazy
from .models import Post

# Create your views here.
# path('', HomePage.as_view(), name='blog')
class PostHomePageView(HomePageView):
    templates_name = "posts/home.html"

class PostListPage(TemplateView):
    template_name = "posts/home.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/home.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post