from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product

class TopView(TemplateView):
    template_name= "top.html"

class ProductListView(ListView):
    model = Product
    template_name = "list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name_suffix = '_detail'