from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from domfix.domfix_products.forms import ProductCreateForm, ProductForm, DeleteProductForm
from domfix.domfix_products.models import Product


@login_required
def add_product(request):
    if request.method == 'GET':
        form = ProductCreateForm()
    else:
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = form.save(commit=True)
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'products/product-add-page.html', context)


def details_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'products/product-details-page.html', context)


def edit_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "GET":
        context = {
            'form': ProductForm(initial=product.__dict__),
        }
        return render(request, 'products/product-edit-page.html', context)

    else:
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {
                'form': form,
            }
    return render(request, 'products/product-edit-page.html', context)


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('catalogue')

    form = DeleteProductForm(instance=product)
    context = {
        'form': form,
    }

    return render(request, 'products/product-delete-page.html', context)
