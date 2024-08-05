from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Product


# Create your views here.
def index(request):
    return render(request, "app/index.html")


class CategoryView(View):

    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, "app/category.html", locals())
