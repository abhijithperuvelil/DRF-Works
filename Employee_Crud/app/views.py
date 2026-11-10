from django.db.migrations import serializer
from django.shortcuts import  get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from app.models import Employee
# Create your views here.
from rest_framework.views import APIView
from django.db.models import Q
from app.serializers import EmployeeSerializer, UserSerializer


class Employee_List(APIView):
    def get(self,request):
        #reads all employee records from employee table
        e=Employee.objects.all()
        #convert the qs into python native type using serializer
        serializer_instance=EmployeeSerializer(e,many=True)
        # return responce as json using responce function
        print(serializer_instance.data)
        return Response(serializer_instance.data)
class Employee_Create(APIView):
    def post(self,request):
        #validation+conversion native to model object
        serializer_instance=EmployeeSerializer(data=request.data)
        #check whether the data coming from client is valid if valid it will save to table
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)#sends created object as responce
        #if not valid return the errors
        else:
            return Response(serializer_instance.errors)
class Employee_Update(APIView):
    def put(self,request,i):
        #reads the record matching with id
        e=get_object_or_404(Employee,id=i)
        #fetches the data coming from client
        data=request.data
        #calls Employee Serializer class for deserialization
        serializer_instance=EmployeeSerializer(instance=e,data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


class Employee_Detail(APIView):
    def get(self,request,i):
        #reads employee record matching with id
        e=get_object_or_404(Employee,id=i)
        #calls serializer class used for conversion
        serializer_instance=EmployeeSerializer(e)
        #sends responce back to client
        return Response(serializer_instance.data)

class Employee_Partial(APIView):
    def patch(self,request,i):
        #reads the record matching with id
        e=Employee.objects.get(id=i)
        #fetches the data coming from client
        data=request.data
        #calls Employee Serializer class for deserialization
        serializer_instance=EmployeeSerializer(instance=e,data=data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


class Employee_Delete(APIView):
    def delete(self,request,i):
        e=get_object_or_404(Employee,id=i)
        e.delete()
        return Response({"message":"deleted"})

# class SearchApi(APIView):
#     def get(self,request):
#         data=request.query_params.get('search')
#         e=Employee.objects.filter(Q(name__icontains=data)|
#                                   Q(place__icontains=data)|
#                                   Q(gender__icontains=data) |
#                                   Q(designation__icontains=data))
#         serializer_instance=EmployeeSerializer(e,many=True)
#         return Response(serializer_instance.data)
from rest_framework import generics
class SearchApi(APIView):
        queryset=Employee.objects.all()
        serializer=EmployeeSerializer
        filter_backends=[SearchFilter]
        search_fields=['title','director','language','year']
class Register(APIView):
    def post(self,request):
        #validation+conversion native to model object
        serializer_instance=UserSerializer(data=request.data)
        #check whether the data coming from client is valid if valid it will save to table
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)#sends created object as responce
        #if not valid return the errors
        else:
            return Response(serializer_instance.errors)