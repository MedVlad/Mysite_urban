from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
# def index_class(request):
#     return render(request,"second_task/index_class.html")
class Index_class(TemplateView):
    template_name = "second_task/index_class.html"


def index_function(request):
    return render(request, "second_task/index_function.html")
