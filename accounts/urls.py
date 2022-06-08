from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
 ]