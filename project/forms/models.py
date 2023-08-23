from django.db import models

# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse



class Inform(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name=['information']),
    added_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]} : {self.category}'

    def get_absolute_url(self):
        return reverse('product_search', args=[str(self.id)])


class Category(models.Model):
    NEWS = "NW"
    ARTICLES = 'AT'

    fields = ([NEWS, 'News'],
                [ARTICLES, "Articles"])
    category = models.CharField(max_length=100, choices= fields, unique=True)
