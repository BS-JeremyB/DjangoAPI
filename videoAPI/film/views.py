from .models import Film
from .serializers import FilmSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import viewsets

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

# class FilmList(ListCreateAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer

# class FilmDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer

# class FilmList(APIView):

#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return  [AllowAny()]
#         else:
#             return  [IsAuthenticated()]

#     def get(self, request, format=None):
#         films = Film.objects.all()
#         serializer = FilmSerializer(films, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = FilmSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class FilmDetail(APIView):

#     def get_object(self, pk):
#         try:
#            return Film.objects.get(pk=pk)
#         except:
#             raise NotFound(detail="Le film n'existe pas !")
        
#     def get(self, request, pk):
#         film = self.get_object(pk)
#         serializer = FilmSerializer(film, context={'request': request})
#         return Response(serializer.data)
    

#     def put(self, request, pk):
#         film = self.get_object(pk)
#         serializer = FilmSerializer(film, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         film = self.get_object(pk)
#         film.delete()
#         return Response({'message': 'Le film a été supprimé'}, status=status.HTTP_204_NO_CONTENT)




