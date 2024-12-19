from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render






def index(request):
    punkt = ['Главная', 'Магазин', 'Корзина']
    data = {'punkt_menu':punkt}
    return render(request, "fourth_task/index.html", context=data)


def market(request):
    context_market = {'games': ['Snow spinner', 'Dcs word', 'I76']}
    data = context_market
    return render(request, "fourth_task/market.html", context=data)


def cart(request):
    return render(request, "fourth_task/cart.html")


from django.shortcuts import render


