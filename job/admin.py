from django.contrib import admin
from .models import Apply , Job , Category

class ApplyAdmin(admin.ModelAdmin):
    list_filter = ('student', 'job','date')


admin.site.register(Apply,ApplyAdmin)
admin.site.register(Job)
admin.site.register(Category)