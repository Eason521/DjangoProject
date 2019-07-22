from django.urls import path
from LoginApp import views

app_name = "LoginApp"
urlpatterns = [
    path('login/', views.login),
    path('quit/', views.quits),
    path('register/', views.register),
    path('', views.index, name="index"),
    path('nameValid/', views.nameValid),
    path('passwordValid/', views.passwordValid),
]
