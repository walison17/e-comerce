# coding=utf-8

from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import generic

class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    paginate_by = 3

product_list = ProductListView.as_view()
# a variavel que mandada para o contexto que será exibido em product_list.hmlt é o nome do modelo minusculo = product
# mais underline mais list, ficaria assim = product_list. Mas se você quiser pode definir um nome diferente criando a
# seguinte variavel: context_object_name = 'o nome que vc bota aqui é a variavel que é mandada para página html'

class CategoryListView(generic.ListView):
    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)