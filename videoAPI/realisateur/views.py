from django.views.decorators.csrf import csrf_exempt
from .models import Realisateur
from .serializers import RealisateurSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.

# POST > Creation - GET > liste
@csrf_exempt
def realisateur_list(request): 
    if request.method == 'GET':
        realisateurs = Realisateur.objects.all()
        serializer = RealisateurSerializer(realisateurs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RealisateurSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
# PUT > mise à jour - DELETE > Supprimer - GET > le detail
def realisateur_detail(request, pk):

    try:
        realisateur = Realisateur.objects.get(pk=pk)
    except:
        return JsonResponse({'error': 'Le réalisateur n\'existe pas'}, status=404)
    
    if request.method == 'GET':
        serializer = RealisateurSerializer(realisateur)
        return JsonResponse(serializer.data)
    

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RealisateurSerializer(realisateur, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        realisateur.delete()
        return JsonResponse({'message': 'Le réalisateur a été supprimé'}, status=204)
