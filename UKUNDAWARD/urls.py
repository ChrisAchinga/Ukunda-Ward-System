from django.contrib import admin
from django.urls import path 
from bursary import views as V


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', V.landingPage),
]
