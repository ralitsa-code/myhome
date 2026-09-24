from django.shortcuts import render, redirect, get_object_or_404
from feature.forms import FeatureForm
from feature.models import Feature


def feature_list(request):
    search = request.GET.get('search', '').strip()

    features = Feature.objects.all()
    if search:
        features = features.filter(name__icontains=search)

    return render(
        request,
        'feature/feature_list.html',
        {'features': features,
         'search': search,
         }
    )


def create_feature(request):
    if request.method == "POST":
        form = FeatureForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('features-list')
    else:
        form = FeatureForm()

    return render(
        request,
        'feature/create_feature.html',
        {'form': form}
    )

def edit_feature(request, feature_id):
    feature = get_object_or_404(Feature, pk=feature_id)

    if request.method == "POST":
        form = FeatureForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('features-list')
    else:
        form = FeatureForm(instance=feature)

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
    if request.method == "POST":
        feature.delete()
        return redirect('features-list')
    else:
        return render(
            request,
            'feature/delete_feature.html',
            {
                'feature_id': feature_id,
                'feature': feature
            }
        )