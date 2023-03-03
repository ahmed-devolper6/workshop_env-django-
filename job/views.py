from django.shortcuts import redirect, render
from .models import Job , Apply
from django.core.paginator import Paginator
from .form import  JobForm , ApplyForm , AcceptFrom
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
from django.db.models import Q
from django.core.mail import send_mail
from accounts.models import StudentProfile


# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    ## filters
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj, "myfilter": myfilter}
    return render(request, "job/job_list.html", context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.student = request.user
            myform.status = 'send'
            myform.save()
            return redirect(reverse("jobs:job_applyes"))
    form = ApplyForm()
    context = {"job": job_detail, 'form1':form}
    return render(request, "job/job_detail.html", context)


@login_required
def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save()
            return redirect(reverse("jobs:job_list"))
    else:
        form = JobForm()

    return render(request, "job/add_job.html", {"form": form})


def studentapplyes(request):
    student_applyes = Apply.objects.filter(student = request.user)
    return render(request,'job/student_applyes.html',{'apply':student_applyes})


def trace(request,id):
    student_applyes = Apply.objects.get(id=id)
    return render(request,'job/apply_list.html',{'apply':student_applyes})



def companys_list(request):
    '''
    studnets_proflie --> apply[jobs:comapny]
    '''
    comapny_job = Job.objects.get(owner = request.user)
    studnet_applyes = Apply.objects.filter(job = comapny_job , status = 'accept')
    return render(request,'job/company_applyes.html',{'apply':studnet_applyes})





from django.shortcuts import  get_object_or_404

def trace_student(request, id):
    student_apply = get_object_or_404(Apply, id=id)
    student = get_object_or_404(StudentProfile, user=student_apply.student)

    if request.method == "POST":
        status = request.POST.get('status_company')
        if bool(status):
            student_apply.status_company = 'accept'
            student_apply.save()
            print('done')
            return redirect(reverse("jobs:company_applyes"))
        else:
            student_apply.status_company = 'regret'
            student_apply.save()

    return render(request, 'job/student_detail.html', {'profile': student, 'job': student_apply})