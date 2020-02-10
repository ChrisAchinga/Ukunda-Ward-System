from django.contrib import admin
from django.urls import path
from bursary import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.landingPage, name='home'),
    path('chart/', v.chartView, name='chart')
]
