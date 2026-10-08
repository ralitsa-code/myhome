from django.shortcuts import render

from property.models import Property


def index(request):
    properties = Property.objects.filter(active=True).order_by('-created_at')[:3]

    return render(
        request,
        'index.html',
        {'properties': properties}
    )

