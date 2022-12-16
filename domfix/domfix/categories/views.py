from django.shortcuts import render

from domfix.domfix_products.models import Product


def catalogue(request):
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'categories/catalogue.html', context)


def dry_construction_products(request):
    products = Product.objects.filter(category='DRY_CONSTRUCTION_PRODUCT')
    context = {
        'products': products
    }
    return render(request, 'categories/dry-construction-products-page.html', context)


def thermal_insulation_products(request):
    products = Product.objects.filter(category='THERMAL_INSULATION_PRODUCT')
    context = {
        'products': products
    }
    return render(request, 'categories/thermal-insulation-products-page.html', context)


def water_supply_and_sanitation_products(request):
    products = Product.objects.filter(category='WATER_SUPPLY_AND_SANITATION_PRODUCT')
    context = {
        'products': products
    }
    return render(request, 'categories/water-supply-and-sanitation-products-page.html', context)


def construction_chemistry_products(request):
    products = Product.objects.filter(category='CONSTRUCTION_CHEMISTRY_PRODUCT')
    context = {
        'products': products
    }
    return render(request, 'categories/construction-chemistry-products-page.html', context)


def tools_products(request):
    products = Product.objects.filter(category='TOOLS_PRODUCT')
    context = {
        'products': products
    }
    return render(request, 'categories/tools-products-page.html', context)


def painting_products(request):
    products = Product.objects.filter(category='PAINTING_PRODUCTS')

    context = {
        'products': products
    }
    return render(request, 'categories/painting-products-page.html', context)


