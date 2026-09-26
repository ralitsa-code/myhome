from django.shortcuts import render, get_object_or_404, redirect

from property.forms import PropertyForm
from property.models import Property


def properties_list(request):
    properties = Property.objects.all()

    return render(
        request,
        'property/properties_list.html',
        {'properties': properties}
    )

def property_details(request, property_id):
    real_estate = get_object_or_404(
        Property.objects.select_related(
            'broker',
            'neighborhood',
            'neighborhood__city'
        ),
        id=property_id
    )

    return render(
        request,
        'property/property_details.html',
        {'property': real_estate}
    )

def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('properties-list')
    else:
        form = PropertyForm()

    return render(
        request,
        'property/create_property.html',
        {'form': form}
    )
