from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Company , Student , CompanyProfile , StudentProfile , User , Batches , Faculty
# Register your models here.
admin.site.register(Company)
admin.site.register(Student)
admin.site.register(CompanyProfile)
admin.site.register(StudentProfile)
admin.site.register(User, UserAdmin)
admin.site.register(Batches)
admin.site.register(Faculty)