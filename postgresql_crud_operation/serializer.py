from django.db import models
from rest_framework import serializers
from .models import Employee_details

class Employee_serialize(serializers.ModelSerializer):
    class Meta:
        model = Employee_details
        fields = '__all__'

        
