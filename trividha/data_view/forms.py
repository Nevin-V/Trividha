from django import forms
from form.models import participant_details


class eventForm(forms.ModelForm):
    class Meta:
        model = participant_details
        fields = ['events']