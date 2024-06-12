from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogPostListCreate.as_view(), name='blog_post_list_create'),
    path('blog/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blog_post_rup'),
]
