from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Song, Artiste
from .serializers import SongSerializer, ArtisteSerializer


@api_view(('GET', 'POST',))
def song_list(request):
    if request.method == "GET":
        queryset = Song.objects.all()
        serializer = SongSerializer(queryset, many=True)
        return Response({"is_successful":serializer.data})

    elif request.method == "POST":
        data = request.data
        serializer = SongSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"is_successful":True})


@api_view(('GET', 'POST', 'DELETE'))
def song_details(request, id):
    if request.method == "GET":
        queryset = Song.objects.get(id=id)
        serializer = SongSerializer(queryset, many=True)
        return Response({"is_successful": serializer.data})

    elif request.method == "PUT":
            serializer = SongSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"is_successful": True})

    elif request.method == "DELETE":
        queryset = Song.objects.get(id=id)
        queryset.delete()
        return Response({"is_successful": True})


@api_view(('GET', 'POST',))
def artiste_list(request):
    if request.method == "GET":
        queryset = Artiste.objects.all()
        serializer = ArtisteSerializer(queryset, many=True)
        return Response({"is_successful":serializer.data})

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArtisteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"is_successful":True})