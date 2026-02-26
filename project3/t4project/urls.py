from django.contrib import admin
from django.urls import path
from app4 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', views.news, name='news'),
    
]
