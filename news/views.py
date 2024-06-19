from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Category
from .forms import NewsForm
from .filters import PostFilter
from django.urls import reverse_lazy
from django.contrib import messages

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
        messages.success(self.request, "Категория успешно создана.")
        return super(CreateCategory,self).form_valid(form)

class UpdateCategory(LoginRequiredMixin,UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories')

    def form_valid(self, form):
        messages.success(self.request, "Категория успешно обновлена.")
        return super(UpdateCategory,self).form_valid(form)
    

class DeleteCategory(LoginRequiredMixin,DeleteView):
    model = Category    
    success_url = reverse_lazy('categories')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Проверяем наличие постов в категории
        if Post.objects.filter(category=self.object).exists():
            messages.error(request, "Невозможно удалить категорию, так как с ней связаны посты.")
            return redirect(self.success_url)  # Редиректим на список категорий, если есть посты
        
        # Если постов нет, вызываем метод delete класса DeleteView
        response = super(DeleteCategory, self).delete(request, *args, **kwargs)
        messages.success(request, "Категория успешно удалена.")
        return response
    


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
    
    def dispatch(self, request, *args, **kwargs):
        if not Category.objects.exists():
            messages.warning(self.request, "Нет категорий. Создайте категорию и повторите попытку создания поста.")
            return redirect(reverse_lazy('create-category'))
        return super(CreatePost, self).dispatch(request, *args, **kwargs)
    
class UpdatePost(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = reverse_lazy('posts')
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