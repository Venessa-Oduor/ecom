from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
]