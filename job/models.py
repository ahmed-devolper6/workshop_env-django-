from django.db import models
from django.utils.text import slugify
from accounts.models import  Company , StudentProfile , Student
from django.utils import timezone
from django.utils.html import format_html
# Create your models here.
status = (
    ('accept','accept'),
    ('regret','regret'),
)
COMPANY = (
    ('accept','accept'),
    ('regret','regret'),
)


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extension)

class Job(models.Model):  # table
    owner = models.ForeignKey(Company, related_name="job_owner", on_delete=models.CASCADE)
    description = models.TextField(max_length=250)
    title = models.CharField(max_length=100)  #
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    Responsibility = models.TextField(max_length=250)
    Benefits = models.TextField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    location = models.CharField(max_length=20)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name



class Apply(models.Model):
    student = models.ForeignKey(Student, related_name = 'student_apply',on_delete= models.SET_NULL, null = True , blank = True)
    job = models.ForeignKey(Job, related_name='job_apply',on_delete= models.SET_NULL , null = True , blank = True)
    status = models.CharField(max_length=25,choices=status,null=True,blank=True)
    cover_letter = models.TextField(max_length=50)
    date = models.DateField(default=timezone.now)
    status_company = models.CharField(max_length=10, choices=COMPANY, null=True, blank=True)


    def __str__(self):
        return f"{str(self.student)} -  {str(self.job)} "

