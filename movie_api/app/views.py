from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from app import serializers
from rest_framework import status
from .serializers import MovieSerializer
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
        print(data)


        return Response({"msg":"success"})