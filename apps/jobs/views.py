from django.shortcuts import render
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job
from .serializers import JobSerializer, JobListSerializer
from apps.accounts.permissions import IsRecruiterOrReadOnly, IsOwnerOrReadOnly

# Create your views here.
class JobListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsRecruiterOrReadOnly]
    filter_backends    = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields   = ['work_type', 'experience_level', 'location', 'is_active']
    search_fields      = ['title', 'company', 'skills_required']
    ordering_fields    = ['salary_min', 'salary_max', 'created_at']
    ordering           = ['-created_at']

    def get_queryset(self):
        return Job.objects.filter(is_active=True).select_related('recruiter')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return JobListSerializer
        return JobSerializer


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Job.objects.all().select_related('recruiter')
    serializer_class   = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return [permissions.IsAuthenticated()]


class RecruiterJobsView(generics.ListAPIView):
    serializer_class   = JobListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(
            recruiter=self.request.user
        ).select_related('recruiter').order_by('-created_at')