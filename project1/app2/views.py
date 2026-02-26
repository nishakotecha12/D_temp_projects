from django.shortcuts import render

# Create your views here.
def loginpage(request):
    return render(request,'app2/loginpage.html')
