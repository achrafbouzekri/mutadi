"""Posts URL configuration"""
from django.urls import path

from .views import (
    add_post_view,
    category_view,
    delete_post_view,
    post_detail_view,
    post_list_view,
    search_results_view,
    update_post_view,
)

urlpatterns = [
    path("post_list/", post_list_view, name="post_list"),
    path("post_detail/<int:pk>", post_detail_view, name="post_detail"),
    path("add_post/", add_post_view, name="add_post"),
    path("post_detail/edit/<int:pk>", update_post_view, name="update_post"),
    path("post_detail/<int:pk>/remove", delete_post_view, name="delete_post"),
    path("category/<str:cats>/", category_view, name="category"),
    path("search/", search_results_view, name="search_results"),
]
