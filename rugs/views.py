from django.shortcuts import get_object_or_404, render
from .models import Category


def home(request):
    return render(request, "index.html")


def categories(request):
    categories_qs = Category.objects.filter(is_active=True)
    return render(request, "categories.html", {"categories": categories_qs})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    return render(request, "category_detail.html", {"category": category})
