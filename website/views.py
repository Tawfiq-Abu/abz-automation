from django.shortcuts import render,redirect

from django.views.generic import TemplateView, ListView
from django.contrib.auth import get_user_model
from django.conf import settings


from utils.mailing import Util as MailUtil



from .models import Metric, TeamMember,Product,ProductFeature,Service
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