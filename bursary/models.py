from django.db import models

# general details of all applicants
class Applicants(models.Model):
    first_name = models.CharField(max_length=100, help_text='Enter First Name')
    middle_name = models.CharField(max_length=100, help_text='Enter Middle Name')
    last_name = models.CharField(max_length=100, help_text='Enter Last Name')

    GENDER_OPTIONS = (
        ('n', 'none'),
        ('m', 'Male'),
        ('f', 'Female'),
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_OPTIONS,
        default='n',
        help_text='Choose between Male or Female'
    )

    class Meta:
        verbose_name_plural = 'Applicants Details'

    def __str__(self):
        return self.first_name +' ' +self.last_name