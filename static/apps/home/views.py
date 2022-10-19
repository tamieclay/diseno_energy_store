# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import get_object_or_404
from .models import MainProducts,FeaturedProducts
from store.models import Order



class HomePage(TemplateView):
    model = MainProducts
    template_name = "home/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = MainProducts.objects.get(id=1)
        context['prod'] = MainProducts.objects.get(id=2)
        context['pro'] = MainProducts.objects.get(id=3)
        ''' context['pr'] = MainProducts.objects.get(id=4)
        context['p'] = MainProducts.objects.get(id=5) '''
        
        return context

class OrderListView(ListView):
    model = Order
    template_name= "home/admin.html"
    
class OrderDetailView(DetailView):
    model = Order
    template_name= "home/index.html"
    
   


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
