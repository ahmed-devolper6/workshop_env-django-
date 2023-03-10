from django.urls import path, re_path
from .views import home , report

app_name = 'dashborad'

urlpatterns = [
    path('' ,home, name = 'report'),
    path('reports/' ,report, name = 'table')
]