from django.urls import path
from .views import home, PostList, CreatePost, UpdatePost,DeletePost, CategoryList, CreateCategory, UpdateCategory, DeleteCategory

urlpatterns = [
    path('',home, name='home'),
    path('categories/', CategoryList.as_view(), name="categories"),
    path('category/create/' , CreateCategory.as_view(), name="create-category"),
    path('category/update/<int:pk>', UpdateCategory.as_view(), name="update-category"),
    path('category/delete/<int:pk>', DeleteCategory.as_view(), name="delete-category"),
    path('posts/', PostList.as_view(), name="posts"),
    path('post/create/' , CreatePost.as_view(), name="create-post"),
    path('post/update/<int:pk>', UpdatePost.as_view(), name="update-post"),
    path('post/delete/<int:pk>', DeletePost.as_view(), name="delete-post"),
]