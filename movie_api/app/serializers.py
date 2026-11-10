from email import message

from django.core.mail import send_mail
from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import User
from django.core.mail import send_mail
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
    def create(self,validated_data):
        #for creating a user account
        u=User.objects.create_user(**validated_data)
        u.save()
        send_mail(
            subject="Welcome to Our Application",
            message= "Thank You For Signing up for an account",
            from_email="spectorking6@gmail.com",
            recipient_list=[u.email,],
            fail_silently=True
        )
        #for creating a super user account
        # u=User.objects.create_superuser(**validated_data)
        return u