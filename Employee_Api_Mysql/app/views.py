from functools import partial
from typing import Any

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from app.models import Employee
from app.serializers import EmployeeSerializer

# # Create your views here.
# class Employee_Create(APIView):
#     def post(self,request):
#         serializer_instance=EmployeeSerializer(data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
#
# class Employee_List(APIView):
#     def get(self,request):
#         e=Employee.objects.all()
#         serializer_instance=EmployeeSerializer(e,many=True)
#         return Response(serializer_instance.data)
# class Employee_Detail(APIView):
#     def get(self,request,i):
#         e=get_object_or_404(Employee,id=i)
#         serializer_instance=EmployeeSerializer(e)
#         return Response(serializer_instance.data)
# class Employee_Update(APIView):
#     def put(self,request,i):
#         e=get_object_or_404(Employee,id=i)
#         serializer_instance=EmployeeSerializer(instance=e,data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
# class Employee_Partial(APIView):
#     def patch(self,request,i):
#         e=get_object_or_404(Employee,id=i)
#         serializer_instance=EmployeeSerializer(instance=e,data=request.data,partial=True)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
# class Employee_Delete(APIView):
#     def delete(self,request,i):
#         e=get_object_or_404(Employee,id=i)
#         e.delete()
#         return Response({"message":"Deleted"})
#
#
from rest_framework import mixins,generics
#
# class EmployeeList(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     def get(self,request):
#         return self.list(request)
# class EmployeeCreate(mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def post(self,request):
#         return self.create(request)
# class EmployeeDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
# class EmployeeUpdate(mixins.UpdateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def put(self,request,pk):
#         return self.update(request,pk)
# class EmployeePartial(mixins.UpdateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def patch(self,request,pk):
#         return self.partial_update(request,pk)
# class EmployeeDelete(mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
# class EmployeeList(generics.ListAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
# class EmployeeCreate(generics.CreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
# class EmployeeDetail(generics.RetrieveAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
# class EmployeeUpdate(generics.UpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
# class EmployeeDelete(generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
# using View Sets
from rest_framework import viewsets
class EmployeeView(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer