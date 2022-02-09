from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('about/', views.About.as_view(), name="about"),
    path('finchs/', views.FinchList.as_view(), name = "finch_list")
]