from rest_framework import serializers
from .models import Student


# Student Serialize
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("name", "age")
