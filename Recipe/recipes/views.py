from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from recipes.models import RecipeModel
from recipes.serializers import RecipeSerializer


# Create your views here.
class ListCreate(APIView):
    def post(self,request):
        serializer_instance=RecipeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        r=RecipeModel.objects.all()
        serializer_instance = RecipeSerializer(r, many=True)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)

class RetrieveUpdateDelete(APIView):
    def get(self,request,i):
        r=get_object_or_404(id=i)
        serializer_instance=RecipeSerializer(r)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
    def put(self,request,i):
        r=get_object_or_404(RecipeModel,id=i)
        serializers_instance=RecipeSerializer(instance=r,data=request.data)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,i):
        r=get_object_or_404(RecipeModel,id=i)
        serializers_instance=RecipeSerializer(instance=r,data=request.data,partial=True)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,i):
        r=get_object_or_404(RecipeModel,id=i)
        r.delete()
        return Response({"message":"deleted"})



