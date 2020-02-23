from django.shortcuts import render
    
# landing page views
def landingPage(request):
    return render(request, 'bursary/index.html')

# admin page view
def adminPage(request):
    return render(request, 'bursary/admin.html')

# charts views
def chartView(request):
    return render(request, 'bursary/chart-chartjs.html')

#apply bursar view
def bursaryView(request):
    return render(request, 'bursary/bursary_form_component.html')

#all applicants view
def applicantsView(request):   
    return render(request, 'bursary/applicants.html')

#secondary applicants view
def sec_applicantsView(request):
    return render(request, 'bursary/sec_applicants.html')

#all applicants view
def uni_applicantsView(request):
    return render(request, 'bursary/uni_applicants.html')

#login view
def loginView(request):
    return render(request, 'bursary/login.html')

#profile view 
def profileView(request):
    return render(request, 'bursary/profile.html')

#contact view
def contactView(request):
    return render(request, 'bursary/contact.html')

#404 view
def notFoundView(request):
    return render(request, 'bursary/404.html')
