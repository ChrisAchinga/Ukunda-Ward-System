from django.contrib import admin
from .models import Applicants, TertiaryApplicants, SecondaryApplicants

admin.site.register(Applicants)
admin.site.register(TertiaryApplicants)
admin.site.register(SecondaryApplicants)