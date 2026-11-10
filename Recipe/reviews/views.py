from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status


from reviews.models import ReviewModel
from rest_framework.response import Response
from reviews.serializer import ReviewSerializer


# Create your views here.
class Review(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    def post(self,request):
        u=request.user
        serializer_instance= ReviewSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=u)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class ReadReview(APIView):
    def get(self,request,pk):
        reviews=ReviewModel.objects.filter(recipe=pk)
        serializer_instance=ReviewSerializer(reviews,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
#update and delete
class UpdateReview(APIView):
    def put(self,request,pk):
        r=get_object_or_404(ReviewModel,id=pk)
        serializer_instance=ReviewSerializer(instance=r,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
# class PartialUpdateReview(APIView):
#     def patch(self, request, pk):
#         r=get_object_or_404(ReviewModel, id=pk)
#         serializer_instance = ReviewSerializer(instance=r, data=request.data,partial=True)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
class DeleteReview(APIView):
    def delete(self, request, pk):
        r=get_object_or_404(ReviewModel, id=pk)
        r.delete()
        return Response({"message":"Deleted"})