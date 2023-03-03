from django.urls import include, path

from . import views


app_name = "job"

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path("add", views.add_job, name="add_job"),
    path('applyes', views.studentapplyes, name="job_applyes"),
    path('applye_list', views.companys_list, name="company_applyes"),
    path('student_detial/<int:id>', views.trace_student, name="trace_studnet"),
    path('applyes/<int:id>', views.trace, name="trace_applyes"),
    path("<str:slug>", views.job_detail, name="job_detail"),
    
]
