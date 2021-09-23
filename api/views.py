
import re
from django.shortcuts import render

from .pagenaion import CustomPagination
# Create your views here.
#------------------------------------------------------------
from rest_framework import viewsets,generics
from api.models import Book, LibUser, RentBook
from api.serializers import BookSerializer, LibUserSerializer,RentBookSerializer, BookCatelogySerilazer
from rest_framework.response import Response
from rest_framework import status
from .models import BookCatelogy
#------------------------------------------------------------

#Bu yerda view Set yaratib olamiz 

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)





class LibuserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer
    pagination_class = CustomPagination
    

class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer  

#--------------------------------------------------------------------------

#list Get
class BookCatelogyListView(generics.ListAPIView):
    queryset = BookCatelogy.objects.all()
    serializer_class = BookCatelogySerilazer

#Post
class BookCatelogyListCreate(generics.CreateAPIView):
    queryset = BookCatelogy.objects.all()
    serializer_class = BookCatelogySerilazer

#post va get yozish va uqush
class BookCatelogyListCreateView(generics.ListCreateAPIView): #yuqoridagi 2ta view birlashmasi Create va view uchun
    queryset = BookCatelogy.objects.all()
    serializer_class = BookCatelogySerilazer

#retrieveView bu id bilan kursatadi get <INT:pk>
class BookCatelogyRetrieveView(generics.RetrieveAPIView): #yuqoridagi 2ta view birlashmasi Create va view uchun
    queryset = BookCatelogy.objects.all()
    serializer_class = BookCatelogySerilazer


#Update qiladi id bialn oladi <int:pk.
class BookCatelogyUpdateView(generics.UpdateAPIView): #yuqoridagi 2ta view birlashmasi Create va view uchun
    queryset = BookCatelogy.objects.all()
    serializer_class = BookCatelogySerilazer


# get and put (update)
class BookCatelogyUpdateRetrieveView(generics.RetrieveUpdateAPIView): #yuqoridagi 2ta view birlashmasi Create va view uchun
    queryset = BookCatelogy.objects.all()
    serializer_class = BookCatelogySerilazer

#Delete  index bilan
class BookCatelogyDestroyView(generics.DestroyAPIView): #yuqoridagi 2ta view birlashmasi Create va view uchun
    queryset = BookCatelogy.objects.all()
    serializer_class = BookCatelogySerilazer
    