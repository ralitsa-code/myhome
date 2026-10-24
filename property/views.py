from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from property.forms import PropertyForm, DeletePropertyForm
from property.models import Property


def properties_list(request):
    search = request.GET.get('search', '').strip()
    status = request.GET.get('status', 'active')

    properties = Property.objects.all()

    if status == 'active':
        properties = properties.filter(active=True)
    elif status == 'inactive':
        properties = properties.filter(active=False)

    if search:
        properties = properties.filter(
            neighborhood__city__name__icontains=search)

    return render(
        request,
        'property/properties_list.html',
        {'properties': properties,
         'search': search,
         'status': status}
    )

    paginator


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


def edit_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property-details', property_id)
    else:
        form = PropertyForm(instance=property)

    return render(
        request,
        'property/edit_property.html',
        {'form': form,
         'property': property
         }
    )


def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    form = DeletePropertyForm(instance=property)

    if request.method == 'POST':
        property.delete()
        return redirect('properties-list')

    return render(
        request,
        'property/delete_property.html',
        {'form': form,
         'property': property
         }
        )

