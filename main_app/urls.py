from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('about/', views.About.as_view(), name="about"),
    path('finchs/', views.FinchList.as_view(), name = "finch_list"),
    path('finchs/new/', views.FinchCreate.as_view(), name = "finch_create"),
    path('finchs/<int:pk>', views.FinchDetail.as_view(), name= "finch_detail"),
    path('finchs/<int:pk>/update', views.FinchUpdate.as_view(), name= "finch_update")
]