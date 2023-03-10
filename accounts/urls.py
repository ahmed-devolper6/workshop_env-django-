from django.urls import include, path

from . import views
from .api import StudentProfileAPIView

app_name = "accounts"

urlpatterns = [
    path('profile/' , views.proflie , name='profile'),
    path('profile/api' , StudentProfileAPIView.as_view() , name='profile'),
]
