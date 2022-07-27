from django.urls import path

from .views import HomeView, OrderView

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('order/', OrderView.as_view(), name='order')
]