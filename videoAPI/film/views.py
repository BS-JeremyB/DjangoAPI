from .models import Film
from .serializers import FilmSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound



class FilmList(APIView):
    def get(self, request, format=None):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FilmDetail(APIView):

    def get_object(self, pk):
        try:
           return Film.objects.get(pk=pk)
        except:
            raise NotFound(detail="Le film n'existe pas !")
        
    def get(self, request, pk):
        film = self.get_object(pk)
        serializer = FilmSerializer(film)
        return Response(serializer.data)
    

    def put(self, request, pk):
        film = self.get_object(pk)
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        film = self.get_object(pk)
        film.delete()
        return Response({'message': 'Le film a été supprimé'}, status=status.HTTP_204_NO_CONTENT)




