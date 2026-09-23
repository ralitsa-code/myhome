from django.shortcuts import render, redirect

from neighbourhood.forms import NeighbourhoodForm
from neighbourhood.models import Neighbourhood


def neighbourhood_list(request):
    search = request.GET.get('search', '').strip()

    neighbourhoods = Neighbourhood.objects.all()

    if search:
        neighbourhoods = neighbourhoods.filter(name__icontains=search)


    return render(
        request,
        'neighborhoods/neighbourhoods_list.html',
        {'neighbourhoods': neighbourhoods,
         'search': search,
         }
    )

def create_neighbourhood(request):
    if request.method == "POST":
        form = NeighbourhoodForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('neighbourhood-list')
    else:
        form = NeighbourhoodForm()

    return render(
        request,
        'neighborhoods/create_neighbourhood.html',
        {'form': form}
    )