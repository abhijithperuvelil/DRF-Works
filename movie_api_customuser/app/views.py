from idlelib.rpc import request_queue

from django.shortcuts import render, get_object_or_404
from django.templatetags.i18n import language
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from app import serializers
from rest_framework import status
from django.db.models import Q
from .serializers import MovieSerializer
from .serializers import UserSerializer
# Create your views here.
class MovieCreate(APIView):
    def post(self,request):
        serializer_instance=MovieSerializer(data=request.data)
        if serializer_instance.is_valid():
            print(serializer_instance.validated_data)
            director=serializer_instance.validated_data['director']
            print(director)
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class MovieList(APIView):
    def get(self,request):
        m=Movie.objects.all()
        serializers_instance=MovieSerializer(m,many=True)
        return Response(serializers_instance.data,status=status.HTTP_200_OK)
class MovieDetial(APIView):
    def get(self,request,i):
        m=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(m)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
class MovieUpdate(APIView):
    def put(self,request,i):
        m=get_object_or_404(Movie,id=i)
        data=request.data
        serializer_instance=MovieSerializer(instance=m,data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_404_NOT_FOUND)
class MoviePatch(APIView):
    def patch(self,request,i):
        m=get_object_or_404(Movie,id=i)
        data=request.data
        serializer_instance=MovieSerializer(instance=m,data=data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_404_NOT_FOUND)
class MovieDelete(APIView):
    def delete(self,request,i):
        m=get_object_or_404(Movie,id=i)
        m.delete()
        return Response({"message":"deleted"},status=status.HTTP_200_OK)

class SearchApiView(APIView):
    def get(self,request):
        #fetches the keyword from the query params
        data=request.query_params.get('search')
        #reads all records matching with the keyboard from db table using filter
        m=Movie.objects.filter(Q(title__icontains=data)|
                               Q(director__icontains=data)|
                                Q(language__icontains=data))
        print(data)
        serializer_instance=MovieSerializer(m,many=True)
        return Response(serializer_instance.data)
class Register(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
