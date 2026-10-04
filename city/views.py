
from django.shortcuts import render, redirect, get_object_or_404

from city.forms import CityCreateForm, CityUpdateForm, CityDeleteForm
from city.models import City
from myhome.forms import SearchForm


def cities_list(request):
    form = SearchForm(request.GET or None)
    cities = City.objects.all()

    if request.method == "GET":
        if form.is_valid():
            query = form.cleaned_data['query']
            cities = City.objects.filter(name__icontains=query)


    return render(
        request,
        'cities/cities_list.html',
        {'cities': cities,
        'form': form,
         }
    )

def create_city(request):
    form = CityCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cities-list')

    return render(
        request,
        'cities/create_city.html',
        {'form': form}
    )

def edit_city(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    form = CityUpdateForm(request.POST or None, instance=city)

    if form.is_valid():
        form.save()
        return redirect('cities-list')

    return render(
        request,
        'cities/edit_city.html',
        {
            'form': form,
            'city': city
        }
    )

def delete_city(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    form = CityDeleteForm(instance=city)

    if request.method == "POST":
        city.delete()
        return redirect('cities-list')

    return render(
        request,
        'cities/delete_city.html',
        {
            'form': form,
        }
    )