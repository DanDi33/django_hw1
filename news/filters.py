import django_filters
from .models import Post, Category

class PostFilter(django_filters.FilterSet):
    # category = django_filters.ChoiceFilter(choices=Post.category)
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    # published_on = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = []
        