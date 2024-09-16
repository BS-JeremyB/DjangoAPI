from django.views.decorators.csrf import csrf_exempt
from .models import Realisateur
from .serializers import RealisateurSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

# POST > Creation - GET > liste
@api_view(['GET', 'POST'])
def realisateur_list(request): 
    if request.method == 'GET':
        realisateurs = Realisateur.objects.all()
        serializer = RealisateurSerializer(realisateurs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RealisateurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT','DELETE'])
# PUT > mise à jour - DELETE > Supprimer - GET > le detail
def realisateur_detail(request, pk):

    try:
        realisateur = Realisateur.objects.get(pk=pk)
    except:
        return Response({'error': 'Le réalisateur n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RealisateurSerializer(realisateur)
        return Response(serializer.data)
    

    elif request.method == 'PUT':
        serializer = RealisateurSerializer(realisateur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        realisateur.delete()
        return Response({'message': 'Le réalisateur a été supprimé'}, status=status.HTTP_204_NO_CONTENT)




