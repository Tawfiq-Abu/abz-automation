from django.urls import path

from .views import HomeView, OrderView,getformdata

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('order/', OrderView.as_view(), name='order'),
    path('formdata/',getformdata,name='getformdata'),
]