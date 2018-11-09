from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    products = Product.objects.order_by('-date_added')[:5]
    
    print(products)
    context = {
        'products': products,
    }

    template = loader.get_template('products/index.html')

    return HttpResponse(template.render(context, request))