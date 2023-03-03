from django.shortcuts import render , redirect
from .models import CompanyProfile , StudentProfile
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login 
from django.contrib import messages

def proflie(request):
    if request.user.role == 'STUDENT':
        studnet = StudentProfile.objects.get(user = request.user)
        return render(request, 'accounts/profile.html', {'stu':studnet})
    if request.user.role == 'COMPANY':
        company = CompanyProfile.objects.get(user = request.user)
        return render(request, 'accounts/profile.html', {company:'company'})
    if request.user.is_superuser:
        redirect('/admin')
    return render(request, 'accounts/profile.html', {})
    
from django.shortcuts import render
from slick_reporting.views import SlickReportView
from slick_reporting.fields import SlickReportField
from job.models import Apply
# Create your views here.
class SimpleListReport(SlickReportView):    
    report_model = Apply
    template_name = 'slick_reporting/simple_report.html'
    date_field = 'date'
    columns = ['date', 'student', 'job', 'status', 'cover_letter','status_company']
    
