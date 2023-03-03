from django import forms

from .models import  Job , Apply



class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        exclude = ("slug",)


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['cover_letter']


class AcceptFrom(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['status_company']