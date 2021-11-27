from django.shortcuts import render

from .models import Attraction


def index_main(request):
    latest = Attraction.objects.all()
    return render(request, "index.html", {"attractions": latest})


def index(request, pk):
    current = Attraction.objects.get(id=pk)
    name = current.name
    description = current.description
    image = current.image
    context = {
        'name': name,
        'description': description,
        'image': image,
    }
    return render(request, "att.html", context)
