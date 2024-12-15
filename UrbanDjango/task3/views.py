from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# class index(TemplateView):
#     template_name = "thrid_task/index.html"
# class market(TemplateView):
#     template_name = "thrid_task/market.html"
# class cart(TemplateView):
#     template_name = "thrid_task/cart.html"


context = {'li_1':'Главная','li_2':'Магазин','li_3':'Корзина'}

def index(request):
    return render(request, "thrid_task/index.html",context=context)

def market(request):
    return render(request, "thrid_task/market.html")

def cart(request):
    return render(request,"thrid_task/cart.html")