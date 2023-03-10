from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import StudentProfile
from .serializers import StudentProfileSerializer

class StudentProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        student_profile = StudentProfile.objects.get(user=request.user)
        serializer = StudentProfileSerializer(student_profile)
        return Response(serializer.data)