# django forms
from django import forms
from models import Applicants, TertiaryApplicants, SecondaryApplicants  

# General Registration Form
class ApplicantForm(forms.Form):
    pass

# Tertiary Applicants
class TertiaryForm(forms.Form):
    pass

# High School Applicants
class SecondaryForm(forms.Form):
    pass