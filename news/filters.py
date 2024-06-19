import django_filters
from .models import Post, Category
from django.utils import timezone
from datetime import timedelta

class PostFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    CHOICES = (
        ('today', 'Сегодня'),
        ('week', 'За неделю'),
        ('month', 'За месяц'),
    )

    ordering = django_filters.ChoiceFilter(choices=CHOICES, method='filter_by_time', empty_label=None)

    class Meta:
        model = Post
        fields = {
            'category': ['exact'],
        }

    def filter_by_time(self, queryset, name, value):
        if value == 'today':
            start_date = timezone.now().date()
            return queryset.filter(created_at__date=start_date)
        if value == 'week':
            start_date = timezone.now().date() - timedelta(days=7)
            return queryset.filter(created_at__date__gte=start_date)
        if value == 'month':
            start_date = timezone.now().date() - timedelta(days=30)
            return queryset.filter(created_at__date__gte=start_date)
        return queryset