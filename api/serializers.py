# api qanday tur qanday kurinishini shu yerga kursatamiz
#Bu fayl asosiy vazifasi malumotlarni  json kurinishga utkazib berish 

#Bu yerda models.py yaratilgan classlarimizni shu kurinishda ulab chiqamiz

from django.db.models import fields
from rest_framework import routers, serializers
from . import models
from .models import Book,LibUser,RentBook,BookCatelogy


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'




class LibUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibUser
        fields = '__all__'
        

class RentBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentBook
        fields = '__all__'
        

class BookCatelogySerilazer(serializers.ModelSerializer):
    class Meta:
        model = BookCatelogy
        fields = '__all__'