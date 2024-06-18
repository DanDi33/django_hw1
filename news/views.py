from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Category
from .forms import NewsForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    posts = Post.objects.all()    
    return render(request, "home.html", {'posts': posts, 'title': 'Главная страница'})

class ShowPost(DetailView):
    model = Post
    template_name = "post.html"
    # context_object_name = "task"

    def get_queryset(self):
        base_qs = super(ShowPost,self).get_queryset()
        print(f"base_qs - {base_qs}")
        return base_qs

class CategoryList(LoginRequiredMixin,ListView):
    model = Category
    template_name = "news/categories.html"
    context_object_name = "categories"

    # def get_context_data(self, * ,object_list = None , **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks'] = context['tasks'].filter(user=self.request.category)
    #     context['desc'] = "It's only test , no more"
    #     return context

class CreateCategory(LoginRequiredMixin,CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories')
    # form_class = CreateCategoryForm
    # template_name = "news/create_category.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was create succesfully !")
        return super(CreateCategory,self).form_valid(form)

class UpdateCategory(LoginRequiredMixin,UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        messages.success(self.request, "The task was update succesfully !")
        return super(UpdateCategory,self).form_valid(form)
    
    # def get_queryset(self):
    #     base_qs = super(UpdateCategory,self).get_queryset()
    #     return base_qs.filter(user = self.request.user)

class DeleteCategory(LoginRequiredMixin,DeleteView):
    model = Category    
    success_url = reverse_lazy('categories')
    # context_object_name = "task"

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted succesfully !")
        return super(DeleteCategory, self).form_valid(form)
    
    # def get_queryset(self):
    #     base_qs = super(TaskDelete,self).get_queryset()
    #     return base_qs.filter(user = self.request.user)

class PostList(LoginRequiredMixin,ListView):
    model = Post
    template_name = "news/posts.html"
    context_object_name = "posts"

    def get_context_data(self, * ,object_list = None , **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user=self.request.user)
        # context['desc'] = "It's only test , no more"
        # print(f"context - {context}")
        return context

class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    success_url = reverse_lazy('posts')
    form_class = NewsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was create succesfully !")
        return super(CreatePost,self).form_valid(form)
    
class UpdatePost(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = reverse_lazy('categories')
    form_class = NewsForm

    def form_valid(self, form):
        messages.success(self.request, "The task was update succesfully !")
        return super(UpdatePost,self).form_valid(form)
    
class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post    
    success_url = reverse_lazy('posts')
    # context_object_name = "task"

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted succesfully !")
        return super(DeletePost, self).form_valid(form)