from django.shortcuts import render
from rest_framework.views import APIView
from patients.models import AppointmentModel
from rest_framework.response import Response
from patients.serializers import PatientSerializer,AppointmentSerializer
from rest_framework import status
from datetime import datetime,timedelta,time
from rest_framework.permissions import  IsAuthenticated
from rest_framework.authentication import BasicAuthentication

# Create your views here.
class Appointment(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer_instance=AppointmentSerializer(data=request.data)
        if serializer_instance.is_valid():
            data=serializer_instance.validated_data
            d=data["doctor"]
            date=data['appointment_date']
            token=0
            appoint_time=time(9,0,0)
            a=AppointmentModel.objects.filter(doctor=d,appointment_date=date).last()
            if a:
                token=a.token_number+1
                appoint_time=(datetime.combine(date,a.appoint_time)+timedelta(minutes=15)).time()
            else:
                token=1
            serializer_instance.save(token_number=token,appoint_time=appoint_time)
            response={
                "status":"Appointment Booked",
                "booking_data":serializer_instance.data}
            return Response(response,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class PatientRegister(APIView):
    def post(self,request):
        serializer_instance=PatientSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)