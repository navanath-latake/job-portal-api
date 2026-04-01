from rest_framework import serializers
from .models import Job


class JobListSerializer(serializers.ModelSerializer):
    recruiter_email = serializers.EmailField(source='recruiter.email', read_only=True)

    class Meta:
        model  = Job
        fields = [
            'id', 'title', 'company', 'location',
            'work_type', 'experience_level',
            'salary_min', 'salary_max',
            'skills_required', 'is_active',
            'deadline', 'recruiter_email', 'created_at',
        ]
        read_only_fields = ['id', 'recruiter_email', 'created_at']


class JobSerializer(serializers.ModelSerializer):
    recruiter_email = serializers.EmailField(source='recruiter.email', read_only=True)

    class Meta:
        model  = Job
        fields = [
            'id', 'title', 'company', 'location',
            'work_type', 'experience_level',
            'description', 'salary_min', 'salary_max',
            'skills_required', 'is_active',
            'deadline', 'recruiter_email', 'created_at',
        ]
        read_only_fields = ['id', 'recruiter_email', 'created_at']

    def validate(self, attrs):
        salary_min = attrs.get('salary_min')
        salary_max = attrs.get('salary_max')
        if salary_min and salary_max and salary_min > salary_max:
            raise serializers.ValidationError(
                {'salary_min': 'salary_min cannot be greater than salary_max.'}
            )
        return attrs

    def create(self, validated_data):
        validated_data['recruiter'] = self.context['request'].user
        return super().create(validated_data)