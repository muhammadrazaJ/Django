from django.db import models

# I want to create a Student model for a CRUD app. Fields: name (char), email (email), age (integer). Create Django model code.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name
# This model represents a student with fields for name, email, and age.
# It includes a string representation method to return the student's name.
from django.urls import path, include
# This file defines the URL patterns for the 'students' app.
from . import views

