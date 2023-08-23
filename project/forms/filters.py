from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Inform, Category

class ProductFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='added_at',
        lookup_expr='exact',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
        model = Inform
        fields = ['name', 'description']

    # class Meta:
    #     model = Product
    #     fields = {
    #         'name': ['incontains'],
    #         'category': ['icontains'],
    #         'date': ['gt']
    #     }

