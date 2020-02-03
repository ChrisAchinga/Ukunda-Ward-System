from django.contrib import admin
from .models import Applicants


# Creating Admin Models
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender')
    list_filter = ('first_name', 'last_name', 'gender',)


admin.site.register(Applicants, ApplicantAdmin)
