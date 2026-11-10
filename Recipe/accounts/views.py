from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from accounts.serializer import UserSerializer

# Create your views here.
class UserRegister(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)