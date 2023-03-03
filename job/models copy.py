from django.db import models
from django.utils.text import slugify
from accounts.models import  Company , StudentProfile , Student
from django.utils import timezone
# Create your models here.
status = (
    ('send','send'),
    ('admin', 'admin'),
    ('company', 'company'),
    ('accept', 'accept'),
)

JOB_TYPE = (
    ("workshops", "workshops"),
    ("traninng", "traninng"),
)


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extension)


class Job(models.Model):  # table
    owner = models.ForeignKey(
        Company, related_name="job_owner", on_delete=models.CASCADE
    )
    description = models.TextField(max_length=250)
    title = models.CharField(max_length=100)  #
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    Responsibility = models.TextField(max_length=250)
    Benefits = models.TextField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    type_job = models.CharField(max_length=30,choices=JOB_TYPE,null=True) 
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
    job = models.ForeignKey(Job, related_name = 'Job_apply',on_delete= models.SET_NULL , null = True , blank = True)
    status = models.CharField(max_length=25,choices=status)
    cover_letter = models.TextField(max_length=50)
    date = models.DateField(default=timezone.now)
    company_accept = models.BooleanField(default=False)

    def __str__(self):
        return str(self.student)

