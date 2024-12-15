from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class index(TemplateView):
    template_name = "thrid_task/index.html"
class market(TemplateView):
    template_name = "thrid_task/market.html"
class cart(TemplateView):
    template_name = "thrid_task/cart.html"
