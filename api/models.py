from django.db import models

# Create your models here.

#Class larimizni shu yerda yaratib olamiz

class Book(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class LibUser(models.Model):
    name = models.CharField(max_length= 100)
    def __str__(self) -> str:
        return self.name


class RentBook(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(LibUser, on_delete=models.CASCADE)
    rentDate = models.DateTimeField(auto_now_add=True)
    reterneddate = models.DateTimeField(null=True,blank=True)
    def __str__(self) -> str:
        return self.rentDate



class BookCatelogy(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name