from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from .models import Product, Customer
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "app/index.html")


def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")


class CategoryView(View):

    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())
    # locals() is used to access the local symbol table in Python.
    # Symbol table: It is a data structure created by a compiler
    # that is used to store all information needed to execute a program.


class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title.val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()

        return render(request, 'app/customer registration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # if the user is successfully registered pass the message;Congratulations!
            messages.success(request, "Congratulations! You have successfully registered.")
        else:
            messages.warning(request, "Please try again.")
        return render(request, 'app/customer registration.html', locals())


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, zipcode=zipcode)
            reg.save()
        return render(request, 'app/profile.html', locals())
