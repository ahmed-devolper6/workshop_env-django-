from django.urls import include, path

from . import views
from .api import JobList , JobDetail , StudentApplyList , ApplyToJob

app_name = "job"

urlpatterns = [
    path("", views.job_list, name="job_list"),
    path('applyes', views.studentapplyes, name="job_applyes"),
    path('applye_list', views.companys_list, name="company_applyes"),
    path('student_detial/<int:id>', views.trace_student, name="trace_studnet"),
    path('applyes/<int:id>', views.trace, name="trace_applyes"),
    path("<str:slug>", views.job_detail, name="job_detail"),
    #api
    path("JobList/",JobList.as_view() , name="job_list_api"),
    path("JobDetail/<int:pk>",JobDetail.as_view() , name="JobDetail_api"),
    path("StudentApplyList/",StudentApplyList.as_view() , name="StudentApplyList_api"),
    path("ApplyToJob/",ApplyToJob.as_view() , name="ApplyToJob_api"),
    
    
]
