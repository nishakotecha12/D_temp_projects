from django.contrib import admin
from django.urls import path
from table_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index_view, name="home"),
    path('students/', students_view, name="students"),
    path('players/', player_view, name="players"),
]
