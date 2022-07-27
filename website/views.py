from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'website/index.html'

class OrderView(TemplateView):
    template_name = 'website/order.html'