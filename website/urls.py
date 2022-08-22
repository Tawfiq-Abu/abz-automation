from django.urls import path

from .views import HomeView, OrderView, getformdata, add_to_basket,basket_update

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('order/', OrderView.as_view(), name='order'),
    path('formdata/',getformdata,name='getformdata'),
    
    path('cart/add/', add_to_basket, name='cart-add'),
    path('cart/update/', basket_update, name='cart-update'),


]