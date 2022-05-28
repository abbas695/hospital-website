# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)

class patient(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    gender =models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    medical_report = models.TextField()	
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    patient_bill = models.PositiveIntegerField()

    def __str__(self):
        return self.name    

class complain(models.Model):
    complainant = models.CharField(max_length=50)
    complainant_last = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    reason = models.TextField()	
    details = models.TextField()	
    message = models.TextField()	
    file = models.FileField()
    gender = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)

    def __str__(self):
        return self.reason           


class Doctor(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    salary = models.PositiveIntegerField()	
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    shift = models.IntegerField()
    patients = models.ManyToManyField(patient, blank=True, related_name='treated_patients')
    # spicialities = models.ManyToManyField(patient, blank=True, related_name='treated_patients')


    def __str__(self):
        return self.first_name + " " + self.second_name 

class Doctors_qualification(models.Model):
    name = models.CharField(max_length=100)
    id_doctor =models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Doctors_spiciality(models.Model):
    name = models.CharField(max_length=100)
    id_doctor = models.PositiveIntegerField()
    def __str__(self):
        return self.name  


class patient_appointment_data(models.Model):
    appointment_place = models.CharField(max_length=255)
    appointment_time = models.PositiveIntegerField()
    id_doctor = models.PositiveIntegerField()
    id_patient = models.PositiveIntegerField()
    
 
class nurse(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    salary = models.PositiveIntegerField()	
    shift = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.second_name 

class account(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    fk_doctor = models.ForeignKey(Doctor, on_delete=models.SET_DEFAULT, default=1)
    fk_nurse = models.ForeignKey(nurse, on_delete=models.SET_DEFAULT, default=1)
    fk_patient = models.ForeignKey(patient, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.user_name       

class medical_company(models.Model):
    market_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    engineer_name = models.CharField(max_length=100)
    engineer_phone = models.CharField(max_length=20)
    PPM_date = models.DateTimeField()
    caliberation_date = models.DateTimeField()

    def __str__(self):
        return self.market_name       

class medical_device(models.Model):
    name = models.CharField(max_length=100)
    last_PPM_date = models.DateTimeField()
    last_caliberation_date = models.DateTimeField()
    fk_market_name = models.ForeignKey(medical_company, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name

class test(models.Model):
    test_type = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    average_time = models.PositiveIntegerField()
    id_patient = models.PositiveIntegerField()
    id_medical_device = models.PositiveIntegerField()
    id_doctor = models.PositiveIntegerField()
    def __str__(self):
        return self.test_type           