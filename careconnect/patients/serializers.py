from rest_framework import serializers
from django.contrib.auth.models import User

import doctor
from patients.models import AppointmentModel
from datetime import datetime
class AppointmentSerializer(serializers.ModelSerializer):
        class Meta:
            model=AppointmentModel
            fields="__all__"
            read_only_fields=['id','appointment_time','token_number','created_at']

        def validate(self,validated_data):
            appointment_date=validated_data['appointment_date']
            todays_date=datetime.now().date()
            d=validated_data['doctor']

            if appointment_date<todays_date:
                raise serializers.ValidationError("Invalid date")

            #25 slots ---> appointment full
               #find the last record
                #check its token number reaches 25,if yes raise error
            last_record= AppointmentModel.objects.filter(doctor=d,appointment_date=appointment_date).last()
            if last_record:
                if last_record.token_number>=25:
                    raise serializers.ValidationError("Appointment is full")
            return validated_data
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u
