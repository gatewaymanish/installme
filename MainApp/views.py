# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render,get_object_or_404
from .models import SetupTemplate, Steps

# Create your views here.

def landing(request):
    categories = SetupTemplate.objects.order_by().values_list('category',flat=True).distinct()
    context = {'categories':categories}
    return render(request,'index.html',context)



def productlist(request,category):
    prodlist = SetupTemplate.objects.filter(category=category)
    context = {'prodlist':prodlist}
    return render(request,'productlist.html',context)


def howtosetupview(request,id):
    qsetsetup = SetupTemplate.objects.filter(id=id)
    category = qsetsetup.values_list('category', flat=True)[0]
    prodlist = SetupTemplate.objects.filter(category=category)
    # print prodlist
    step = Steps.objects.filter(setup_id=id).order_by('id')
    context = {'step':step, 'qsetsetup':qsetsetup,'prodlist':prodlist }
    return render(request,'howtosetup.html', context)












# def product(request, prod_id):
#     queryset = Product.objects.all()
#     query = request.GET.get("q")
#     if query:
#         prod_id = ''
#         queryset = queryset.filter(
#             Q(productName__icontains=query) |
#             Q(productCategory__icontains=query) |
#             Q(productManufacturer__icontains=query) |
#             Q(productManufacturerCountry__icontains=query)
#         )
#         context = {'prodSearchList': queryset}
#         if len(queryset) != 0:
#             return render(request, 'productSearch.html', context)
#         else:
#             return render(request, "404.html")
#     else:
#         queryset = Product.objects.filter(productId=prod_id)
#         if len(queryset) != 0:
#             context = {'qs': queryset}
#             return render(request, 'product.html', context)
#         else:
#             return render(request, "404.html")