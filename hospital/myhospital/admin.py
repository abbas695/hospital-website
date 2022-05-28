from django.contrib import admin
from .models import User,Doctor,complain,Doctors_qualification,Doctors_spiciality,patient_appointment_data,patient,nurse,account,medical_company,test,medical_device

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Doctors_qualification)
admin.site.register(Doctors_spiciality)
admin.site.register(patient_appointment_data)
admin.site.register(patient)
admin.site.register(nurse)
admin.site.register(account)
admin.site.register(medical_company)
admin.site.register(test)
admin.site.register(medical_device)
admin.site.register(complain)
admin.site.register(User)






