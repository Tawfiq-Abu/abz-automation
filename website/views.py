from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib import messages

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
    
    # messages.info(request, 'Your message has been successfully sent!')
    return redirect('website:home')


class OrderView(TemplateView):
    template_name = 'website/order.html'


def add_to_basket(request):
    session_basket = SessionBasket(request)
    
    if request.method == 'POST':
        # check the type of order and add to the appropriate basket section
        order_type = request.POST.get('order_type')

        if order_type == "product_order":
            product_model_id = int(request.POST.get('product_model_id'))

            # check if product_model is already in basket
            if str(product_model_id) in session_basket.basket['product_orders']:
                print("error here")
                return JsonResponse({"error": "already added"}, status=400)


            # create product order and add to basket 
            product_model = ProductModel.objects.get(pk=product_model_id)
            session_basket.add_product_model(product_model=product_model)
        
        elif order_type == "service_request":
            service_id = int(request.POST.get('service_id'))

            print(str(service_id))
            print(session_basket.basket['service_requests'])
            print(str(service_id) in session_basket.basket['service_requests'])
            # check if service is already in basket
            if str(service_id) in session_basket.basket['service_requests']:
                print("error here")
                return JsonResponse({"error": "already added"}, status=400)

            # create service request and add to basket 
            service = Service.objects.get(pk=service_id)
            session_basket.add_service(service=service)
        
        return JsonResponse({"basket_quantity": session_basket.__len__()})


        

        # basket_length = product_order.basket.product_order_set.count() + product_order.basket.service_request_set.count()

        # # return length of basket
        # return JsonResponse({
        #     'basket_length': basket_length,
        # })

def basket_update(request):
    session_basket = SessionBasket(request)
    if request.method == 'POST':
        product_model_id = int(request.POST.get('product_model_id'))
        product_qty = int(request.POST.get('productqty'))
        session_basket.update_product_order(product_model_id=product_model_id,quantity=product_qty)
        print(session_basket.basket['product_orders'])
        print(product_model_id)
        print(product_qty)
        # get the length of the items in the basket
        basket_quantity = session_basket.__len__()
        # basket_total = basket.get_total_price()
        response = JsonResponse({'basket_quantity':basket_quantity})#'total':basket_total
        return response


def basket_delete(request):
    session_basket = SessionBasket(request)
    if request.method == 'POST':
        # check the type of order and add to the appropriate basket section
        order_type = request.POST.get('order_type')

        if order_type == "product_order":
            product_model_id = int(request.POST.get('product_model_id'))

            # check if product_model is in basket
            if not str(product_model_id) in session_basket.basket['product_orders']:
                print("error here")
                return JsonResponse({"error": "no such product order"}, status=400)

            session_basket.delete_product_order(product_model_id=product_model_id)
            basket_quantity = session_basket.__len__()
            basket_total = session_basket.get_total_price()
            
            response = JsonResponse({
                'basket_quantity':basket_quantity, 
                'total':basket_total
                })
            return response
        
        elif order_type == "service_request":
            service_id = int(request.POST.get('service_id'))

            # check if product_model is in basket
            if not str(service_id) in session_basket.basket['service_requests']:
                print("error here")
                return JsonResponse({"error": "no such service request"}, status=400)

            session_basket.delete_service_request(service_id=service_id)
            basket_quantity = session_basket.__len__()
            basket_total = session_basket.get_total_price()
            
            response = JsonResponse({
                'basket_quantity':basket_quantity, 
                'total':basket_total
                })
            return response


def confirm_basket(request):
    session_basket = SessionBasket(request)
    if request.method == 'POST':
        # creating the basket item
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone_number = request.POST.get('customer_phone_number')
        current_basket = Basket.objects.create(
            customer_name = customer_name,
            customer_email = customer_email,
            customer_phone_number = customer_phone_number
        )
        current_basket.save()

        for i,v in session_basket.basket['product_orders'].items():
            product_model = ProductModel.objects.get(id = int(i))
            quantity = v['quantity']
            total_amount = v['price']
            basket = current_basket

            product_order = ProductOrder.objects.create(
                product_model = product_model,
                quantity = quantity,
                total_amount = total_amount,
                basket = basket
            )
            product_order.save()

        

        response = JsonResponse({})
        return response

        for i,v in session_basket.basket['service_requests'].items():
            service = Service.objects.get(id = int(i))

            service_create=ServiceRequest.objects.create(
                service = service,
                basket = basket
            )
            service_create.save()





        


