from django.db import models

# model for bursary applicant
class Applicant(models.Model):
    first_name = models.CharField(max_length=5)
    middle_name = models.CharField(max_length=5)
    last_name = models.CharField(max_length=5)
    