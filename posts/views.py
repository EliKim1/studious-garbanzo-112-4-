from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.url import reverse_lazy
from .models import Post, Status

# Create your views here.
# path('', HomePage.as_view(), name='blog')
class PostListView(HomePageView):
    templates_name = "posts/list.html"
    model = Post

class DraftPostListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name='draft')
        context['post_list'] = Post.objects.filter(
            author=self.request.user
            ).filter(
                status=pending_status).order_by(
                'created_on').reverse()
        
        return context

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/home.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post