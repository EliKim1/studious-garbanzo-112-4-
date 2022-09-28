from django.urls import path
from .views import (HomePageView, AboutPageView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView, 
    AboutPageView
)

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('about/', AboutPageView.as_view(), name='about'),
]