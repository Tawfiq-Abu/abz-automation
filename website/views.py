from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Metric
# Create your views here.

class HomeView(ListView):
    model = Metric
    context_object_name = "metrics"
    template_name = 'website/index.html'

class OrderView(TemplateView):
    template_name = 'website/order.html'