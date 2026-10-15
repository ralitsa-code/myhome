from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from feature.forms import CreateFeatureForm, DeleteFeatureForm
from feature.models import Feature
from myhome.forms import SearchForm


def feature_list(request):
    form = SearchForm(request.GET or None)
    features = Feature.objects.all()

    if request.method == "GET":
        if form.is_valid():
            query = form.cleaned_data['query']
            features = Feature.objects.filter(name__icontains=query)


    return render(
        request,
        'feature/feature_list.html',
        {'features': features,
         'form': form,
         }
    )

class CreateFeature(CreateView):
    template_name = 'feature/create_feature.html'
    form_class = CreateFeatureForm
    success_url = reverse_lazy('features-list')



class EditFeatureView(UpdateView):
    model = Feature
    template_name = 'feature/edit_feature.html'
    success_url = reverse_lazy('features-list')
    fields = ['name',]




def delete_feature(request, feature_id):
    feature = get_object_or_404(Feature, pk=feature_id)
    form = DeleteFeatureForm(instance=feature)

    if request.method == "POST":
        feature.delete()
        return redirect('features-list')

    return render(
        request,
        'feature/delete_feature.html',
        {
            'form': form,
        }
    )