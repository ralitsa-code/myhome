from django.shortcuts import render

from broker.models import Broker


# Create your views here.
def brokers_list(request):
    brokers = Broker.objects.all()
    return render(
        request,
        'broker/brokers_list.html',
        {'brokers': brokers}
    )