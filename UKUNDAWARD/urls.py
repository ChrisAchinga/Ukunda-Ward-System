from django.contrib import admin
from django.urls import path
from bursary import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.landingPage, name='home'),
    path('index.html/', v.landingPage, name='home'),
    path('chart-chartjs/', v.chartView, name='chart'),
    path('bursary_form_component/', v.bursaryView, name='bursary'),
    path('applicants/', v.applicantsView, name='applicants'),
    path('universityapplicants/', v.uni_applicantsView, name='uni_applicants'),
    path('secondaryapplicants/', v.sec_applicantsView, name='sec_applicants'),
    path('login/', v.loginView, name='login'),
    path('profile/', v.profileView, name='profile'),
    path('contact/', v.contactView, name='contact'),
    path('404/', v.notFoundView, name='notfound')    
]
