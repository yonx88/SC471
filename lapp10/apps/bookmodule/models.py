from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

class Address(models.Model):
    city = models.CharField(max_length=255)

class Student(models.Model):
    name = models.CharField(max_length=255) 
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE) 