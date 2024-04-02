from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter, CharFilter
import django_filters
from django.forms import DateTimeInput
from .models import Post, Category, PostCategory


class PostFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок',
    )

    added_after = DateTimeFilter(
        label='Дата публикации после',
        field_name='time_in',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    category = ModelMultipleChoiceFilter(
        field_name='category_post_many__name',
        queryset=Category.objects.all(),
        label='Категории публикации',
    )

    # class Meta:
    #     model = Post
    #     # fields = '__all__'
    #     fields = {
    #         'title': ['iexact'],
    #     }
