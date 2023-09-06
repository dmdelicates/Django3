from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort", "id")
    if sort == 'max_price':
        sort = "-price"
    elif sort == 'min_price':
        sort = "price"
    phones = Phone.objects.order_by(sort)

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    tel = Phone.objects.get(slug=slug)
    context = {'slug': tel}
    return render(request, template, context)
