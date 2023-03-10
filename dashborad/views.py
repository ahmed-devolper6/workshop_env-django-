from django.shortcuts import render
from job.models import Job , Apply 
from accounts.models import Student , Company , StudentProfile 
from .form import DateRangeForm
# Create your views here.


# Create your views here.
def home(request):
    workshops = Job.objects.all().count()
    applyes = Apply.objects.all().count()
    stundets = Student.objects.all().count()
    companys = Company.objects.all().count()
    form = DateRangeForm(request.POST or None)
    if form.is_valid():
        when = form.cleaned_data['when']
        to = form.cleaned_data['to']
        my_objects = Apply.objects.filter(date__range=[when, to])
    else:
        my_objects = Apply.objects.all()
    context = {'workshops':workshops,'applyes':applyes,'stundets':stundets,'companys':companys,'form': form, 'info': my_objects}
    return render(request , 'dashborad/home.html',context)

def report(request):
    form = DateRangeForm(request.POST or None)
    if form.is_valid():
        when = form.cleaned_data['when']
        to = form.cleaned_data['to']
        my_objects = Apply.objects.filter(date__range=[when, to])
    else:
        my_objects = Apply.objects.all()
    
    context = {'form': form, 'info': my_objects}
    return render(request, 'dashborad/report.html', context)