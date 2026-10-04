from django.shortcuts import render, redirect, get_object_or_404
from feature.forms import CreateFeatureForm, UpdateFeatureForm, DeleteFeatureForm
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


def create_feature(request):
    if request.method == "POST":
        form = CreateFeatureForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('features-list')
    else:
        form = CreateFeatureForm()

    return render(
        request,
        'feature/create_feature.html',
        {'form': form}
    )

def edit_feature(request, feature_id):
    feature = get_object_or_404(Feature, pk=feature_id)

    if request.method == "POST":
        form = UpdateFeatureForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('features-list')
    else:
        form = UpdateFeatureForm(instance=feature)

    return render(
        request,
        'feature/edit_feature.html',
        {
            'form': form,
            'feature_id': feature_id
        }
    )

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