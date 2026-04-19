from django import forms
from .models import Personnel


class PersonnelForm(forms.ModelForm):
  class Meta:
    model = Personnel
    fields = ['full_name','rank_position','unit_section','contact_number']
