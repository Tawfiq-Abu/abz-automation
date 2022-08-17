from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth import get_user_model

from utils.mailing import Util as MailUtil

from .models import Basket, Metric, ProductModel, ProductOrder, ServiceRequest, TeamMember, Product, Service

from .basket import Basket as SessionBasket
# Create your views here.
user = get_user_model()

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



def getformdata(request):
    data = request.POST
    email_body = data['name'] + ' '+ 'response email' + ' '+ data['email'] + '\n' + data['message']
    data = {'email_body': email_body, 'to_email': settings.EMAIL_HOST_USER,
                'email_subject': data['subject']}
    MailUtil.send_email(data)
    print(data)
    return redirect('https://www.google.com')


class OrderView(TemplateView):
    template_name = 'website/order.html'


def add_to_basket(request):
    session_basket = SessionBasket(request)
    
    if request.method == 'POST':
        # check the type of order and add to the appropriate basket section
        order_type = request.POST.get('order_type')

        if order_type == "product_order":
            product_model_id = int(request.POST.get('product_model_id'))
            # create product order and add to basket 
            product_model = ProductModel.objects.get(pk=product_model_id)
            basket = Basket.objects.create()
            product_order = ProductOrder.objects.create(
                product_model=product_model, 
                basket=basket
                )
            session_basket.add_prodcut_order(product_order=product_order)
        
        elif order_type == "service_request":
            service_id = int(request.POST.get('service_id'))
            # create product order and add to basket 
            service = Service.objects.get(pk=service_id)
            basket = Basket.objects.create()
            service_request = ServiceRequest.objects.create(
                service=service, 
                basket=basket
                )
            session_basket.add_service_request(service_request=service_request)
        
        return JsonResponse({"basket_quantity": session_basket.__len__()})


        

        basket_length = product_order.basket.product_order_set.count() + product_order.basket.service_request_set.count()

        # return length of basket
        return JsonResponse({
            'basket_length': basket_length,
        })