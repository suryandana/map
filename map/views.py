from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Coord

def home(request):
    coord = Coord.objects.all()
    # coord_names = list()
    # for elem in coord:
    #     coord_names.append(", ".join([elem.name, elem.description, str(elem.lat), str(elem.lng)]))
    # response_html = '<br>'.join(coord_names)
    # return HttpResponse(response_html)
    
    return render(request, 'map.html', {'coord': coord})
    
def serialize(request):
    data = serializers.serialize("json", Coord.objects.all())
    return JsonResponse(data, safe=False)