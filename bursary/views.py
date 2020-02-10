from django.shortcuts import render
    
# landing page views
def landingPage(request):
    return render(request, 'bursary/index.html')

# admin page view
def adminPage(request):
    return render(request, 'bursary/admin.html')

# charts views
def chartView(request):
    return render(request, 'bursary/charts,html')