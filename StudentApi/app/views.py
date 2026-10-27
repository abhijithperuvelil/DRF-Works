from django.db.migrations import serializer
from django.db.models import Model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializers import StudentSerializer
from app.models import Student


class StudentDetails(APIView):
    def get(self, request):
        s = Student.objects.all().values()
        serializer_instance=StudentSerializer(s,many=True)
        return Response(serializer_instance.data)
class StudentCreate(APIView):
    def post(self,request):
        serializer_instance=StudentSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message":"created"})
        else:
            return Response({"message":"invalid"})
class StudentUpdate(APIView):
    def put(self,request,i):
        s=get_object_or_404(Student,id=i)
        data=request.data
        serializer_instance=StudentSerializer(instance=s,data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
class StudentPartial(APIView):
    def patch(self,request,i):
        s=get_object_or_404(Student,id=i)
        data=request.data
        serializer_instance=StudentSerializer(instance=s,data=data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
class StudentDelete(APIView):
    def delete(self,request,i):
        s=get_object_or_404(Student,id=i)
        s.delete()
        return Response({"message":"Deleted"})

# class StudentCreate(View):
#     def post(self, request):
#         data = loads(request.body)
#         n = data['name']
#         a = data['age']
#         m = data['marks']
#         c = data['course']
#         Student.objects.create(
#             Name=n,
#             Age=a,
#             Course=c,
#             Marks=m
#         )
#         return JsonResponse({"message": "Created"})
# @method_decorator(csrf_exempt, name="dispatch")
# class StudentDelete(View):
#     def delete(self, request, i):
#         s = Student.objects.get(id=i)
#         s.delete()
#         return JsonResponse({"message": "Deleted"})
# @method_decorator(csrf_exempt, name="dispatch")
# class StudentUpdate(View):
#     def put(self, request, i):
#         form_data = request.body
#         data = loads(form_data)
#         s = Student.objects.get(id=i)
#         s.Name = data['Name']
#         s.Age = data['Age']
#         s.Course = data['Course']
#         s.Marks = data['Marks']
#         s.save()
#         return JsonResponse({"Message": "Updated"})
# @method_decorator(csrf_exempt,name="dispatch")
# class StudentPatch(View):
#     def patch(self,request,i):
#         form_data=request.body
#         data=loads(form_data)
#         s=Student.objects.get(id=i)
#         if 'Name' in data:
#             s.Name=data['Name']
#         if 'Age' in data:
#             s.Age=data['Age']
#         if 'Course' in data:
#             s.Course=data['Course']
#         if 'Marks' in data:
#             s.Marks=data['Marks']
#         s.save()
#         return JsonResponse({"Message":"Updated"})