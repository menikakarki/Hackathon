from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
   path("", views.index, name='home'),
   path("about", views.about, name='about'),
   path("services", views.services, name='Services'),
   path("contacts", views.contacts, name='Contacts'),
   path("doctor", views.doctor, name='doctor'),
   path("patient", views.patient, name='patient'),
   path("guest", views.guest, name='guest'),
   path("doctorsignup", views.doctorsignup, name='doctorsignup'),
   path("doctorlogin", views.doctorlogin, name='doctorlogin'),
   path("doctorlogout", views.doctorlogout, name='doctorlogout'),
   path("patientsignup", views.patientsignup, name='patientsignup'),
   path("patientlogin", views.patientlogin, name='patientlogin'),
   path("patientlogout", views.patientlogout, name='patientlogout'),

]
