from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.categories import Category

# Create your views here.

def index(request):
    products=None
    category=Category.get_all_categories();
    categoryID=request.GET.get('category')
    if categoryID:
        products=Product.get_all_categories_by_categoryid(categoryID)
    else:
        products=Product.get_all_product();
    data={}
    data['products']=products
    data['category']=category
    return render(request, 'index.html', data)
