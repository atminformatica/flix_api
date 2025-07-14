#import json
#from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from django.shortcuts import get_list_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from genres.permissions import GenrePermissionClass
from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GenrePermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GenrePermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method== 'GET':           
#         genres_modelorm = Genre.objects.all()
#         #vamos usar list compression - jogar dados para uma lista de dicionarios
#         genres_dicionario = [{'id': genre.id, 'name': genre.name} for genre in genres_modelorm]
#         return JsonResponse(genres_dicionario,safe=False)
#             #safe=false significa que apenas lista de dicionarios podem ser serializados
#     elif request.method=='POST':
#         data = json.loads(request.body.decode('utf-8'))#utf-8 formato strings - aceita ç etc
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse(
#             {'id':new_genre.id, 'name':new_genre.name},
#             status=201,
#         )
    
# @csrf_exempt
# def genre_detail_view(request,pk):
#     genre = get_list_or_404(Genre,pk=pk)
    
#     if request.method=='GET':
#         data = {'id':genre.id, 'name':genre.name}
#         return JsonResponse(data)
#     elif request.method=='PUT':
#         data = json.loads(request.body.decode('utf-8'))#utf-8 formato strings - aceita ç etc
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse(
#             {'id':genre.id, 'name':genre.name},
#             status=201,
#         )
#     elif request.method=='DELETE':
#         genre.remove()
#         return JsonResponse(
#             {'message':'Gênero removido com sucesso!'},
#             status=204,
#         )