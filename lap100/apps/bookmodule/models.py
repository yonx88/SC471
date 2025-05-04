from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

class Address(models.Model):
    city = models.CharField(max_length=255)

class Department(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=255) 
    age = models.IntegerField()

    address = models.ForeignKey(Address, on_delete=models.CASCADE) 
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)   # افتراضياً يتم ربطه بالقسم الأول
    courses = models.ManyToManyField(Course)

