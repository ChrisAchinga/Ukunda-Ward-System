from django.db import models

# model for general bursary applicant information
class Applicant(models.Model):
    # applicant_RegNo = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # date_Registerd = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass



# model for university applicant
# used many:one relationship, with Applicant model 
# degree, diploma, cert
class UniversityApplicant(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=10)

# used many:one relationship, with Applicant model 
# model for college or Technical institute
class TechnicalCollege(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)


# used many:one relationship, with Applicant model 
# model for High school
# national, county, sub-county
class HighSchool(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
