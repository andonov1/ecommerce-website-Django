from django.shortcuts import render, redirect
from django.views import View
from .forms import ProductForm
from .models import Product


def product_list_view(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/product_list.html', context)


class AddProductView(View):
    form_class = ProductForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'products/add_product.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products list')
        return render(request, 'products/add_product.html', {'form': form})


def product_detail_view(request, pk):
    product = Product.objects.get(pk=pk)

    context = {'product': product}
    return render(request, 'products/product_details.html', context)
