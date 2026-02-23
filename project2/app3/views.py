from django.shortcuts import render

# Create your views here.
def registrationpage(request):
    return render(request, 'app3/registrationpage.html')
