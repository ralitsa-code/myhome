from django.shortcuts import render, redirect, get_object_or_404

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

def edit_neighbourhood(request, neighbourhood_id):
    neighbourhood = get_object_or_404(Neighbourhood, pk=neighbourhood_id)

    if request.method == "POST":
        form = NeighbourhoodForm(request.POST, instance=neighbourhood)
        if form.is_valid():
            form.save()
            return redirect('neighbourhood-list')
    else:
        form = NeighbourhoodForm(instance=neighbourhood)

    return render(
        request,
        'neighborhoods/edit_neighbourhood.html',
        {'form': form,
         'neighbourhood': neighbourhood
        }
    )

def delete_neighbourhood(request, neighbourhood_id):
    neighbourhood = get_object_or_404(Neighbourhood, pk=neighbourhood_id)

    if request.method == "POST":
        neighbourhood.delete()
        return redirect('neighbourhood-list')
    else:
        return render(
            request,
            'neighborhoods/delete_neighbourhood.html',
            {'neighbourhood': neighbourhood,
             'neighbourhood_id': neighbourhood_id
             }
        )
