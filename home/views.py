from django.shortcuts import render
from job.models import Job ,  Category
from accounts.models import Company

def homepage(request):
   listed_jobs = Job.objects.count()
   jobs = Job.objects.all()[0:3]
   companys = Company.objects.all()
   category = Category.objects.all()
   return render(request,'home/homepage.html',{'jobs':listed_jobs,'company':companys,'catgory':category,'list':jobs})
