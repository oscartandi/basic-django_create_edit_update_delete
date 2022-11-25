from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    model=Employee
    class Meta:
        model=Employee
        fields="__all__"