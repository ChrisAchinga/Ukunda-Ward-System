from django.shortcuts import render

def landingPage(request):
    return render(request, 'bursary/index.html')