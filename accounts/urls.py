from django.urls import include, path

from . import views

app_name = "accounts"

urlpatterns = [
    path('profile' , views.proflie , name='profile'),
    path('reports' , views.SimpleListReport.as_view() , name='report'),
]
