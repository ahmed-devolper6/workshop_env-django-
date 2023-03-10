from rest_framework import serializers
from .models import StudentProfile

class StudentProfileSerializer(serializers.ModelSerializer):
    faculty = serializers.StringRelatedField()
    batches = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = StudentProfile
        fields = ['user','name', 'faculty', 'batches', 'phone_number', 'cgpa', 'email']
        read_only_fields = ['user']