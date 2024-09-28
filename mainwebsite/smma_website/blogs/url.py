from django.urls import path
from blogs import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/<slug:slug>", views.detail, name="detail"),
    path("category/<category>/",views.blog_category,name="blog_category" ),
    path("create",views.post_blog,name="create_blog"),
]