from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Category
from .forms import NewsForm
from .filters import PostFilter
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.

def home(request):
    queryset = Post.objects.all()
    filter = PostFilter(request.GET, queryset=queryset)

    # Применяем фильтрацию
    queryset = filter.qs

    return render(request, "home.html", {'filter': filter, 'title': 'Главная страница'})

class ShowPost(DetailView):
    model = Post
    template_name = "post.html"

    def get_queryset(self):
        base_qs = super(ShowPost,self).get_queryset()
        print(f"base_qs - {base_qs}")
        return base_qs

class CategoryList(LoginRequiredMixin,ListView):
    model = Category
    template_name = "news/categories.html"
    context_object_name = "categories"


class CreateCategory(LoginRequiredMixin,CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The category was create succesfully !")
        return super(CreateCategory,self).form_valid(form)

class UpdateCategory(LoginRequiredMixin,UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        messages.success(self.request, "The category was update succesfully !")
        return super(UpdateCategory,self).form_valid(form)
    

class DeleteCategory(LoginRequiredMixin,DeleteView):
    model = Category    
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        messages.success(self.request, "The category was deleted succesfully !")
        return super(DeleteCategory, self).form_valid(form)

class PostList(LoginRequiredMixin,ListView):
    model = Post
    template_name = "news/posts.html"
    context_object_name = "posts"

    def get_queryset(self) :
        queryset = super().get_queryset() 
        self.filter = PostFilter(self.request.GET,queryset=queryset)
        return self.filter.qs
    
    def get_context_data(self, * ,object_list = None , **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        return context
    
class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    success_url = reverse_lazy('posts')
    form_class = NewsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The post was create succesfully !")
        return super(CreatePost,self).form_valid(form)
    
class UpdatePost(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = reverse_lazy('categories')
    form_class = NewsForm

    def form_valid(self, form):
        messages.success(self.request, "The post was update succesfully !")
        return super(UpdatePost,self).form_valid(form)
    
class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post    
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        messages.success(self.request, "The post was deleted succesfully !")
        return super(DeletePost, self).form_valid(form)