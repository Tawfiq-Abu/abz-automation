

from .models import ProductOrder, ServiceRequest
from decimal import Decimal


class Basket():


    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {
                "product_orders": {},
                "service_requests": {}
            }
        self.basket = basket

    def clear(self, request):
        self.session = request.session
        self.basket = self.session['skey'] = {}

    def add_prodcut_order(self, product_order):
        '''
        adding and updating the users basket session product_order
        '''
        if product_order:
            product_order_id = str(product_order.id)
            if product_order_id not in self.basket["product_orders"]:
                self.basket["product_orders"][product_order_id] = {
                    'name': str(product_order.product_model),
                    'price': str(product_order.product_model.price),
                    'quantity':product_order.quantity
                    }
         
        self.save()

    def add_service_request(self, service_request):
        '''
        adding and updating the users basket session service_request
        '''
        if service_request:
            service_request_id = str(service_request.id)
            if service_request_id not in self.basket["service_requests"]:
                self.basket["service_requests"][service_request_id] = {
                    'name': service_request.service.name,
                    'price': service_request.service.price
                }
        self.save()
       

    # def __iter__(self):
    #     '''
    #     collect the product_id in the session data to the query the database and return the products
    #     '''
        
    #     product_order_ids  = self.basket['product_orders']
    #     service_request_ids  = self.basket['service_requests']
        
    #     # a custom manager set in the models where it only displays items that are active
    #     product_orders = ProductOrder.products.filter(id__in=product_ids)
    #     basket = self.basket.copy()
        
    #     # including the product into the basket 
    #     for product in products:
    #         basket[str(product.id)]['product'] = product

    #     for item in basket.values():
    #         item['price'] = Decimal(item['price'])
    #         item['total_price'] = item['price']*item['qty']
    #         #return the item
    #         yield item


    def __len__(self):
        '''
        get the basket data and count the quantity of items in it.
        '''
        product_order_count = sum(product_order['quantity'] for product_order in self.basket["product_orders"].values())
        service_request_count = len(self.basket["service_requests"])
        
        return product_order_count + service_request_count

    def get_total_price(self):
        product_orders_total = sum(Decimal(product_order['price']) * product_order['quantity'] for product_order in self.basket['product_orders'].values())
        service_requests_total = sum(Decimal(service_request['price']) for service_request in self.basket['service_requests'].values())
        return product_orders_total + service_requests_total

    def delete_product_order(self, product_order_id):
        product_order_id = str(product_order_id)

        if product_order_id in self.basket["product_orders"]:
            del self.basket["product_orders"][product_order_id]
        self.save()
    
    def delete_service_request(self, service_request_id):
        service_request_id = str(service_request_id)

        if service_request_id in self.basket["service_requests"]:
            del self.basket["service_requests"][service_request_id]
        self.save()
    

    def update_product_order(self,product_order_id, quantity):
        '''
        update product_order values in session data
        '''
        product_order_id = str(product_order_id)
        if product_order_id in self.basket["product_orders"]:
            self.basket["product_orders"][product_order_id]['quantity'] = quantity
        self.save()

    def update_service_request(self,service_request_id, quantity):
        '''
        update service_request values in session data
        '''
        service_request_id = str(service_request_id)
        if service_request_id in self.basket["service_requests"]:
            self.basket["service_requests"][service_request_id]['quantity'] = quantity
        self.save()


    def save(self):
        self.session.modified = True
