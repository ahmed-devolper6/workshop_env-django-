from django import forms
from datetime import datetime

class DateRangeForm(forms.Form):
    when = forms.DateField(input_formats=['%m/%d/%Y'])
    to = forms.DateField(input_formats=['%m/%d/%Y'])

    def clean(self):
        cleaned_data = super().clean()
        when = cleaned_data.get('when')
        to = cleaned_data.get('to')
        if when and to and when > to:
            raise forms.ValidationError('Invalid date range: "when" cannot be after "to".')
        return cleaned_data
