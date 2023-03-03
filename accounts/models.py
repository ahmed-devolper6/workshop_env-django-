from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        COMPANY = "COMPANY", "Company"
    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            self.password = make_password(self.password)
  
            return super().save(*args, **kwargs)


class StudentManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have an email address")
        user = self.model(username=self.normalize_email(username), **extra_fields)
        user.set_password(make_password(password))
        user.save(using=self._db)
        return user
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)


class Student(User):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, role=User.Role.STUDENT, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    base_role = User.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for students"


@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    index = models.IntegerField(max_length=10, null=True , blank=True , default=0)
    faculty = models.ForeignKey('Faculty',on_delete=models.SET_NULL,null=True,blank=True,related_name='students_faculty')
    batches = models.ForeignKey('Batches',on_delete=models.SET_NULL,null=True,blank=True,related_name='students_batches')
    phone_number = models.CharField(max_length=14,null=True,blank=True,default='')
    cgpa = models.FloatField(null=True,blank=True, default=0)
    email = models.EmailField(max_length=20)

    def __str__(self) -> str:
        return str(self.user)
    
class Batches(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
class Faculty(models.Model):
    name = models.CharField(max_length=800)

    def __str__(self) -> str:
        return self.name

class CompanyManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, role=User.Role.COMPANY, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.COMPANY)


class Company(User):
    base_role = User.Role.COMPANY

    teacher = CompanyManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for teachers"


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    loction = models.CharField(max_length=50)
    desc = models.TextField(max_length=250)
    image = models.ImageField(upload_to="company_proflie_img")
    onwer_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25, null=True, blank=True)
    contact_number = models.CharField(max_length=25)

    def __str__(self) -> str:
        return str(self.user)


@receiver(post_save, sender=Company)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "COMPANY":
        CompanyProfile.objects.create(user=instance)
