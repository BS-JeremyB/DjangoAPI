from .models import Realisateur
from .serializers import *
from videoAPI.permissions import IsAdminUser, IsAuthenticatedNoDelete, IsReadOnly
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
class RealisateurViewSet(viewsets.ModelViewSet):
    queryset = Realisateur.objects.all()
    #permission_classes = [IsAdminUser | IsAuthenticatedNoDelete | IsReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['nom', 'date_naissance']
    ordering_fields = ['nom', 'date_naissance']
    #ordering = ['-nom']
    

    def get_serializer_class(self):
        if self.action == 'list':
            return RealisateurListSerializer
        
        return RealisateurSerializer
    

# class RealisateurList(ListCreateAPIView):
#     queryset = Realisateur.objects.all()
#     #serializer_class = RealisateurSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return RealisateurListSerializer
        
#         return RealisateurSerializer

# class RealisateurDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Realisateur.objects.all()
#     serializer_class = RealisateurSerializer

# class RealisateurList(APIView):
#     permission_classes = [IsAdminUser | IsAuthenticatedNoDelete | IsReadOnly]
#     # def get_permissions(self):
#     #     if self.request.method == 'POST':
#     #         return [IsAuthenticated()]
#     #     else:
#     #         return [AllowAny()]
   

#     def get(self, request, format=None):
#         realisateurs = Realisateur.objects.all()
#         serializer = RealisateurListSerializer(realisateurs, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = RealisateurSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class RealisateurDetail(APIView):
#     permission_classes = [IsAdminUser | IsAuthenticatedNoDelete | IsReadOnly]
#     def get_object(self, pk):
#         try:
#            return Realisateur.objects.get(pk=pk)
#         except:
#             raise NotFound(detail="Le réalisateur n'existe pas !")
        
#     def get(self, request,  pk, format=None,):
#         realisateur = self.get_object(pk)
#         serializer = RealisateurSerializer(realisateur, context={'request': request})
#         return Response(serializer.data)
    

#     def put(self, request, pk):
#         realisateur = self.get_object(pk)
#         serializer = RealisateurSerializer(realisateur, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         realisateur = self.get_object(pk)
#         realisateur.delete()
#         return Response({'message': 'Le réalisateur a été supprimé'}, status=status.HTTP_204_NO_CONTENT)




