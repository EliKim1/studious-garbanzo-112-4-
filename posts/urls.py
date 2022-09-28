from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, HomePage, AboutPage,


  
urlpatterns = [
    path('list/', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
    path('', HomePage.as_view(), name='blog'),
    path('', AboutPage.as_view(), name='about'),
]