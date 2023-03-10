from rest_framework import generics, permissions
from .models import Apply, Job
from .serializers import ApplySerializer, JobSerializer


class JobList(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Job.objects.all()


class JobDetail(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentApplyList(generics.ListAPIView):
    serializer_class = ApplySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Apply.objects.filter(student=self.request.user)


class ApplyToJob(generics.CreateAPIView):
    serializer_class = ApplySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        job_id = self.kwargs.get('job_id')
        job = generics.get_object_or_404(Job, id=job_id)
        serializer.save(student=self.request.user, job=job)