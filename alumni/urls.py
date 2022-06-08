from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from alumni import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/updateprofile/<int:pk>/', views.UpdateProfile.as_view(), name="update_profile"),
    
    path('career/', views.CareerCreateView.as_view(), name='career'),
    path('career/update-experience/<int:pk>/', views.UpdateExperice.as_view(), name="update_experience"),
    path('career/delete-experience/<int:pk>/', views.destroyBatch, name="delete_experience"),  

    path('generate-certificate/', views.generate_certificate, name='generate_certificate'),
    # path('career/', views.career),
    path('events/', views.events, name='events'),

    path('opportunity/', views.opportunity, name='opportunities'), 

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
