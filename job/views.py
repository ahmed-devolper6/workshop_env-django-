from django.shortcuts import redirect, render , get_object_or_404
from .models import Job , Apply
from django.core.paginator import Paginator
from .form import  JobForm , ApplyForm , AcceptFrom
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
from django.db.models import Q
from django.core.mail import send_mail
from accounts.models import StudentProfile
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    
    # Exclude jobs that the current user has already applied for
    applied_jobs = Apply.objects.filter(student=request.user).values_list("job__id", flat=True)
    job_list = job_list.exclude(id__in=applied_jobs)
    # filters
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj, "myfilter": myfilter, "message": request.GET.get("message")}
    return render(request, "job/job_list.html", context)

def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.student = request.user
            myform.save()
            message = "You have successfully applied for the job: " + job_detail.title
            return HttpResponseRedirect(reverse('jobs:job_list') + "?message=" + message)

    form = ApplyForm()
    context = {'job': job_detail, 'form1': form}
    return render(request, 'job/job_detail.html', context)


def studentapplyes(request):
    student_applyes = Apply.objects.filter(student = request.user)
    return render(request,'job/student_applyes.html',{'apply':student_applyes})


def trace(request,id):
    student_applyes = Apply.objects.get(id=id)
    return render(request,'job/apply_list.html',{'apply':student_applyes})



def companys_list(request):
    comapny_jobs = Job.objects.filter(owner=request.user)
    studnet_applyes = Apply.objects.filter(job__in=comapny_jobs, status='accept')
    return render(request,'job/company_applyes.html',{'apply':studnet_applyes})

def trace_student(request, id):
    student_apply = get_object_or_404(Apply, id=id)
    student = get_object_or_404(StudentProfile, user=student_apply.student)

    if request.method == "POST":
        status = request.POST.get('status_company')
        if status == 'False':
            student_apply.status_company = 'regret'
            student_apply.save()
        else:
            student_apply.status_company = 'accept'
            student_apply.save()
    return render(request, 'job/student_detail.html', {'profile': student, 'job': student_apply})