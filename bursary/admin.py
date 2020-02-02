from django.contrib import admin
from .models import Applicant, UniversityApplicant, TechnicalCollege, HighSchool

admin.site.register(Applicant)
admin.site.register(UniversityApplicant)
admin.site.register(TechnicalCollege)
admin.site.register(HighSchool)