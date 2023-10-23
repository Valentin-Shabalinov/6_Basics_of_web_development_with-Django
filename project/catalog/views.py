from django.shortcuts import render

from catalog.models import Product, Category

def catalog_contacts(request):
    return render(request, 'main/contacts.html')


def catalog_home(request):
    return render(request, 'main/home.html')


def index(request):
    product_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        'object_list': product_list,
        'category_list': category_list,
        'title': 'Магазин с продуктами'
    }
    return render(request, 'main/index.html', context)


def index_one(request, pk):
    product_list = Product.objects.get(pk=pk)
    context = {
        'object': product_list
    }
    return render(request, 'main/index_one.html', context)

