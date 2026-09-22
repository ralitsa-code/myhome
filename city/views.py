from django.shortcuts import render, redirect, get_object_or_404

from city.forms import CityForm
from city.models import City

def cities_list(request):
    cities = City.objects.all()
    return render(
        request,
        'cities/cities_list.html',
        {'cities': cities}
    )

def create_city(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('cities-list')
    else:
        form = CityForm()

    return render(
        request,
        'cities/create_city.html',
        {'form': form}
    )

def edit_city(request, city_id):
    city = get_object_or_404(City, pk=city_id)

    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('cities-list')
    else:
        form = CityForm(instance=city)

    return render(
        request,
        'cities/edit_city.html',
        {
            'form': form,
            'city': city
        }
    )

def delete_city(request, city_id):
    city = get_object_or_404(City.objects, pk=city_id)
    if request.method == "POST":
        city.delete()
        return redirect('cities-list')
    else:
        return render(
            request,
            'cities/delete_city.html',
            {
                'city_id': city_id,
                'city': city
            }
        )