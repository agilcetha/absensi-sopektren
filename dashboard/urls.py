from django.urls import path
from dashboard import views 

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('logout/', views.logoutPage, name='logoutPage'),
    path('register/', views.registerPage, name='registerPage'),


]
