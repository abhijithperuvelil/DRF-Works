from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Doctor
from .serializers import DoctorSerializer,AdminSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication

from rest_framework.permissions import   IsAdminUser
from rest_framework.response import Response
# Create your views here.
class DoctorListCreate(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    def get(self,request):
        qs = Doctor.objects.all()
        serializer_instance = DoctorSerializer(qs, many=True)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer_instance = DoctorSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

# Reading a specific doctor
# Updating a doctor
# Deleting a doctor
class RetrieveUpdateDelete(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    def get(self,request,i):
        d = get_object_or_404(Doctor, id=i)
        serializer_instance = DoctorSerializer(d)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)

    def put(self,request,i):
        d= get_object_or_404(Doctor, id=i)
        serializer_instance = DoctorSerializer(instance=d, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        d = get_object_or_404(Doctor, id=pk)
        serializer_instance = DoctorSerializer(instance=d, data=request.data, partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        d = get_object_or_404(Doctor, id=pk)
        d.delete()
        return Response({"message": "Record Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

# Filtering doctors based on specialization
class DoctorSearch(APIView):
    def get(self, request):
        data = request.query_params.get('search')
        d = Doctor.objects.filter(specialization=data)
        serializer_instance = DoctorSerializer(d, many=True)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)
class AdminUser(APIView):
    def post(self, request):
        serializer_instance = AdminSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)