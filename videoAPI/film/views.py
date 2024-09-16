from django.views.decorators.csrf import csrf_exempt
from .models import Film
from .serializers import FilmSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def film_list(request): 
    if request.method == 'GET':
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FilmSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
# PUT > mise à jour - DELETE > Supprimer - GET > le detail
def film_detail(request, pk):

    try:
        film = Film.objects.get(pk=pk)
    except:
        return JsonResponse({'error': 'Le réalisateur n\'existe pas'}, status=404)
    
    if request.method == 'GET':
        serializer = FilmSerializer(film)
        return JsonResponse(serializer.data)
    

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FilmSerializer(film, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        film.delete()
        return JsonResponse({'message': 'Le réalisateur a été supprimé'}, status=204)