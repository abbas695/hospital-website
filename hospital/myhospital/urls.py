from django.urls import path
from .views import login_request, Render_sign_up,Render_contact,logout_view , patientSignUpView,DoctorVeiw,NurseVeiw,Render_home,Newqualification,Newcomplain,Newspeciality,R_doctor_test,R_patient_test,R_patient_appointment,NewNurse,NewTest,NewAppointment,Render_patients_data, NewDoctor, Render_medical_devices,Render_doctor_patients_data,Render_medical_companies,Render_nurses,NewPatient,Render_doctors_data,Render_doctor_spicialities,Render_doctor_qualifications,Render_doctor_appointment


urlpatterns = [
    path('', Render_home, name='home'),
    path('medical_devices/', Render_medical_devices, name='medical_devices'),
    path('medical_companies/', Render_medical_companies, name='medical_companies'),
    path('nurses/', Render_nurses, name='nurses'),
    path('doctors/<id>/patients', Render_doctor_patients_data, name='doctor_patients_data'),
    path('doctors_data/', Render_doctors_data, name='doctors_data'),
    path('doctors/<id>/spiciality', Render_doctor_spicialities, name='doctor_spiciality'),
    path('doctors/<id>/qualification', Render_doctor_qualifications, name='doctor_qualification'),
    path('doctors/<id>/appointment', Render_doctor_appointment, name='doctor_appointment'),
    path('patients_data/', Render_patients_data, name='patients_data'),
    path('patients/add', NewPatient, name='create_patient'),
    path('doctors/add', NewDoctor, name='create_doctor'),
    path('Nurse/add', NewNurse, name='create_nurse'),
    path('test/add', NewTest, name='create_test'),
    path('appointment/add', NewAppointment, name='create_appointment'),
    path('patient/<id>/appointment', R_patient_appointment, name='patient_appointment'),
    path('patient/<id>/test', R_patient_test, name='patient_test'),
    path('doctor/<id>/test', R_doctor_test, name='doctor_test'),
    path('complain/add', Newcomplain, name='complain'),
    path('speciality/add', Newspeciality, name='add_speciality'),
    path('qualification/add', Newqualification, name='add_qualification'),
    path('signup/patient/', patientSignUpView.as_view(), name='patient_signup'),
    path('signup/doctor/', DoctorVeiw.as_view(), name='doctor_signup'),
    path('signup/nurse/', NurseVeiw.as_view(), name='nurse_signup'),
    path('login/', login_request, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contact/', Render_contact, name='contact'),
    path('sign_up', Render_sign_up, name='SignUp'),




]
