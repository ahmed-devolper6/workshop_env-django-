from rest_framework import serializers
from .models import Job, Apply
from django.contrib.auth.models import User
from accounts.models import Company
from accounts.models import CompanyProfile 
class CompanyProfileSerializer(serializers.ModelSerializer):
    #username = serializers.CharField(source='user.username')
    class Meta:
        model = CompanyProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    company_profile = CompanyProfileSerializer()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'company_profile']


class JobSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    owner = serializers.SerializerMethodField()
    owner_username = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ['id', 'description', 'title', 'published_at', 'Vacancy', 'Responsibility', 'Benefits', 'location', 'category', 'owner', 'owner_username']

    def get_owner(self, obj):
        company_profile_data = obj.owner.company_proflie
        company_profile_serializer = CompanyProfileSerializer(company_profile_data)
        owner_data = company_profile_serializer.data
        owner_data['image'] = self.context['request'].build_absolute_uri(owner_data['image'])
        return owner_data

    def get_owner_username(self, obj):
        return obj.owner.username

class ApplySerializer(serializers.ModelSerializer):
    job = JobSerializer(source='job_apply',many=True)
    class Meta:
        model = Apply
        fields = ['id','status','cover_letter','date','status_company','job']
