from rest_framework import serializers
from .models import Application
from apps.jobs.serializers import JobListSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    job_detail      = JobListSerializer(source='job', read_only=True)
    applicant_email = serializers.EmailField(source='applicant.email', read_only=True)

    class Meta:
        model  = Application
        fields = [
            'id', 'job', 'job_detail',
            'applicant_email', 'status',
            'cover_letter', 'resume', 'created_at',
        ]
        read_only_fields = ['id', 'applicant_email', 'status', 'created_at', 'job_detail']

    def validate(self, attrs):
        request = self.context['request']
        job     = attrs.get('job')
        if Application.objects.filter(applicant=request.user, job=job).exists():
            raise serializers.ValidationError('You have already applied for this job.')
        return attrs

    def create(self, validated_data):
        validated_data['applicant'] = self.context['request'].user
        return super().create(validated_data)


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Application
        fields = ['id', 'status']