from django.contrib import admin
from django.urls import path
from app2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginpage/', loginpage, name='loginpage'),
]
