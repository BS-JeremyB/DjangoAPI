from django.views.decorators.csrf import csrf_exempt
from .models import Film
from .serializers import FilmSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def film_list(request): 
    if request.method == 'GET':
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
# PUT > mise à jour - DELETE > Supprimer - GET > le detail
def film_detail(request, pk):

    try:
        film = Film.objects.get(pk=pk)
    except:
        return Response({'error': 'Le réalisateur n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FilmSerializer(film)
        return Response(serializer.data)
    

    elif request.method == 'PUT':
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        film.delete()
        return Response({'message': 'Le réalisateur a été supprimé'}, status=status.HTTP_204_NO_CONTENT)