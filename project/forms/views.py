from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .filters import ProductFilter
from .forms import ProductForm
from .models import Inform
from django_filters.rest_framework import DjangoFilterBackend



class ProductsList(ListView):
    model = Inform
    ordering = 'name'
    template_name = 'first_view.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['filterset'] = self.filterset
      return context

   # def search_filter(request):
   #    customer = Product.objects.all()



class ProductDetail(DetailView):
   model = Inform
   template_name = 'an_search.html'
   context_object_name = 'products'


class ProductCreate(CreateView):
   form_class = ProductForm
   model = Inform
   template_name = 'an_create.html'

   def form_valid(self, form):
      product = form.save(commit=False)
      product.quantity = 13
      return super().form_valid(form)


class ProductUpdate(UpdateView):
   form_class = ProductForm
   model = Inform
   template_name = 'an_create.html'


class ProductDelete(DeleteView):
   model = Inform
   template_name = 'an_delete.html'
   success_url = reverse_lazy('product_list')