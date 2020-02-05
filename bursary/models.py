from django.db import models

# general applicants details
class Applicants(models.Model):
    # first name
    first_name = models.CharField(
        "First Name",
        max_length=100,
        help_text="Enter first name"
    )
    # middle name
    middle_name = models.CharField(
        "Middle Name",
        max_length=100,
        help_text="Enter middle name"
    )
    # last name
    last_name = models.CharField(
        "Last Name",
        max_length=100,
        help_text="Enter last name"
    )
    # Date of Birth
    date_of_birth = models.DateField(
        "Date of Birth(DoB)",
        auto_now=False,
        auto_now_add=False,
        help_text="Date of Birth"
    )
    # age
    age = models.IntegerField(
        "Age",
        blank=False
    )
    # date Registerd to system set to aumatically add itself
    date_registered = models.DateTimeField(
        "Date of Registatration",
    )
    # list for gender options
    GENDER_OPTIONS = (
        ('n', 'none selected'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    # select gender
    gender = models.CharField(
        "Gender",
        max_length=1,
        choices=GENDER_OPTIONS
    )
    # parent detail selection
    PARENT_OPTIONS = (
        ('N', 'None Selected'),
        ('M', 'Mother'),
        ('F', 'father'),
    )
    # parent 1
    parent1_relation = models.CharField(
        "Relation With Parent",
        choices=PARENT_OPTIONS,
        max_length=1
    )
    parent1_name1 = models.CharField(
        "Parent First Name",
        max_length=100
    )
    parent1_name2 = models.CharField(
        "Parent Second Name",
        max_length=100
    )
    parent1_IdNo = models.IntegerField(
        "Parent Id No",
    )
    

    # function to auto add date registered
    def was_published_recently(self):
        return self.date_registered >= timezone.now() - datetime.timedelta(days=1)

# Tertiary Education Applicants: University/Colleges/TechnicalInstitutes
class TertiaryApplicants(models.Model):
    pass

# Secondary Education Applicants
class SecondaryApplicants(models.Model):
    pass