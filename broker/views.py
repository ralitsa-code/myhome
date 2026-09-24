from django.shortcuts import render, get_object_or_404, redirect

from broker.forms import BrokerForm
from broker.models import Broker


# Create your views here.
def brokers_list(request):
    search = request.GET.get('search', '').strip()

    brokers = Broker.objects.all()
    if search:
        brokers = brokers.filter(first_name__icontains=search , last_name__icontains=search)

    return render(
        request,
        'broker/brokers_list.html',
        {'brokers': brokers}
    )

def broker_details(request, broker_id):
    broker = get_object_or_404(Broker.objects.prefetch_related('properties'), id=broker_id)
    return render(
        request,
        'broker/broker_details.html',
        {'broker': broker}
    )

def create_broker(request):
    if request.method == "POST":
        form = BrokerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('brokers-list')
    else:
        form = BrokerForm()

    return render(
        request,
        'broker/create_broker.html',
        {'form': form}
    )

def edit_broker(request, broker_id):
    broker = get_object_or_404(Broker, id=broker_id)

    if request.method == "POST":
        form = BrokerForm(request.POST, request.FILES, instance=broker)
        if form.is_valid():
            form.save()
            return redirect('brokers-list')
    else:
        form = BrokerForm(instance=broker)

    return render(
        request,
        'broker/edit_broker.html',
        {'form': form,
        'broker': broker
        }
    )