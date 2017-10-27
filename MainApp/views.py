# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render,get_object_or_404
from .models import SetupTemplate, Steps
import simplejson as json
from django.http import HttpResponse
from django.db import connection
from django.db.models import Q


# Create your views here.
categories = SetupTemplate.objects.order_by().values_list('category', flat=True).distinct()


def landing(request):
    # sqr = SetupTemplate.objects.all().filter(request.GET.get('q'))
    query = request.GET.get("q")
    if query:
        result = SetupTemplate.objects.all().filter(
                    Q(category__icontains=query) |
                    Q(productName__icontains=query) |
                    Q(platformType__icontains=query)

                )
        # print result,"######"
        searchResult = {'result': result, 'categories':categories}
        print searchResult
        return render(request, 'search.html', searchResult)
    else:
        latestsetuplist = SetupTemplate.objects.order_by('-creationTime')[:10][::1]
        # print connection.queries[-1]['sql']
        context = {'categories':categories, 'latestsetuplist':latestsetuplist}
        return render(request,'index.html',context)



def productlist(request,category):
    prodlist = SetupTemplate.objects.filter(category=category)
    context = {'prodlist':prodlist, 'categories':categories}
    return render(request,'productlist.html',context)


def howtosetupview(request,id):
    qsetsetup = SetupTemplate.objects.filter(id=id)
    category = qsetsetup.values_list('category', flat=True)[0]
    prodlist = SetupTemplate.objects.filter(category=category)
    # print prodlist
    step = Steps.objects.filter(setup_id=id).order_by('id')
    context = {'step':step, 'qsetsetup':qsetsetup,'prodlist':prodlist }
    return render(request,'howtosetup.html', context)

def search(request):
    context = {'categories':categories}
    return render(request, 'search.html', context)

# def autocomplete(request):
#     sqr = SetupTemplate.objects.filter(request.GET.get('q', ''))
#     # sqs = SetupTemplate().autocomplete(content_auto=request.GET.get('q', ''))[:5]
#     print sqr,"**********"
#     suggestions = [result.title for result in sqr]
#     # Make sure you return a JSON object, not a bare list.
#     # Otherwise, you could be vulnerable to an XSS attack.
#     the_data = json.dumps({
#         'results': suggestions
#     })
#     return HttpResponse(the_data, content_type='application/json')








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