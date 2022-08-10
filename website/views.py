from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Metric, TeamMember,Product,Feature,Service
# Create your views here.

class HomeView(ListView):
    model = Metric
    context_object_name = "metrics"
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs) :
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'team_member_list': TeamMember.objects.all(),
            'product_list': Product.objects.all(),
            'service_list': Service.objects.all(),

        })
        return context





class OrderView(TemplateView):
    template_name = 'website/order.html'