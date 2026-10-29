
from rest_framework import mixins,generics,viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


from .models import Movie
from .serializers import MovieSerializer
#Mixins
#Api for listing and creating Movie Record
# class MovieListCreate(mixins.ListModelMixin,CreateModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
# #api for read/update/delete exisiting movie record
# class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.put(request,pk)
#     def patch(self,request,pk):
#         return self.partial_update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
#
# class MovieList(generics.ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
# class MovieRetrieve(generics.RetrieveAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
# class MovieUpdate(generics.UpdateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
# class MovieCreate(generics.CreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
# class MovieDelete(generics.DestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
from rest_framework import viewsets
class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
