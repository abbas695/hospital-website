from django.shortcuts import render , redirect
from django.template import loader
from django.http import HttpResponse
from re import template
from django.contrib.auth import login, logout,authenticate
from .models import medical_device ,test
from .models import medical_company
from .models import nurse
from .models import Doctor , User
from .models import patient
from .models import Doctors_spiciality
from .models import Doctors_qualification
from django.views.generic import (CreateView, DeleteView, DetailView, ListView)
from .models import patient_appointment_data , complain
from .forms import NewPatientForm ,NurseSignUpForm,NewcomplainForm,NewDoctorForm ,NewNurseForm ,NewsqualificationtForm, NewAppointmentForm , NewTestForm ,NewspecialitytForm,PatientSignUpForm,DoctorSignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .decorators import patient_required , doctor_required ,nurse_required


class patientSignUpView(CreateView):
    
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/PatientSignUpForm.html'

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/')

class DoctorVeiw(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'registration/DoctorSignUpForm.html'
    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/')

class NurseVeiw(CreateView):
    model = User
    form_class = NurseSignUpForm
    template_name = 'registration/NurseSignUpForm.html'
    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/')        

# Create your views here.
def Render_home(request):

	template = loader.get_template('home.html')

	context = {	}

	return HttpResponse(template.render(context, request))

# Create your views here.
def Render_sign_up(request):

	template = loader.get_template('sign up.html')

	context = {	}

	return HttpResponse(template.render(context, request))    

def Render_contact(request):

	template = loader.get_template('ContactUs.html')

	context = {	}

	return HttpResponse(template.render(context, request))    

@login_required 
# Create your views here.
def Render_medical_devices(request):

    medical_device_data = medical_device.objects.all()
    template = loader.get_template('Medical_DeviceTable.html')
    context = { "medical_device_data":medical_device_data}
    return HttpResponse(template.render(context, request))

@login_required 
# Create your views here.
def Render_medical_companies(request):
    medical_companies_data = medical_company.objects.all()
    template = loader.get_template('Medical_Company.html')
    context = {"medical_companies_data":medical_companies_data}
    return HttpResponse(template.render(context, request))    


# @login_required 
# @nurse_required
# Create your views here.
@login_required 
def Render_nurses(request):
    nurses_data = nurse.objects.all()
    template = loader.get_template('NursessData.html')
    context = {"nurses_data":nurses_data}
    return HttpResponse(template.render(context, request))        

# Create your views here.
def Render_doctor_patients_data(request,id):
    doctor = Doctor.objects.get(id=id)
    patients = doctor.patients.all()
    # print(patients)
    template = loader.get_template('patientsData.html')
    context = {"patients_data":patients}
    return HttpResponse(template.render(context, request))    

# Create your views here.
@login_required 
def Render_patients_data(request):
    patients_data = patient.objects.all()
    template = loader.get_template('patientsData.html')
    context = {"patients_data":patients_data}
    return HttpResponse(template.render(context, request))    

# Create your views here.
@login_required 
def Render_doctors_data(request):
    doctors_data = Doctor.objects.all()
    template = loader.get_template('doctorsdata.html')
    context = {"doctors_data":doctors_data}
    return HttpResponse(template.render(context, request))      

# Create your views here.
@login_required 
def Render_doctor_spicialities(request,id):
    doctors_spiciality_data = Doctors_spiciality.objects.filter(id_doctor = int(id))
    template = loader.get_template('doctors_speciality.html')
    context = {"doctors_spiciality_data":doctors_spiciality_data}
    return HttpResponse(template.render(context, request))      

# Create your views here.
@login_required 
def Render_doctor_qualifications(request,id):
    doctors_qualification_data = Doctors_qualification.objects.filter(id_doctor = int(id))
    template = loader.get_template('doctors_qualifications.html')
    context = {"doctors_qualification_data":doctors_qualification_data}
    return HttpResponse(template.render(context, request))      

# Create your views here.
@login_required 
def Render_doctor_appointment(request,id):
    doctors_appointment_data = patient_appointment_data.objects.filter(id_doctor =int(id) )
    template = loader.get_template('Appointment_Data.html')
    context = {"doctors_appointment_data":doctors_appointment_data}
    return HttpResponse(template.render(context, request))    

# Create your views here.
@login_required 
def R_patient_test(request,id):
    patients_tests = test.objects.filter(id_patient =int(id) )
    template = loader.get_template('tests_Data.html')
    context = {"TestsData":patients_tests}
    return HttpResponse(template.render(context, request)) 

# Create your views here.
@login_required 
def R_doctor_test(request,id):
    doctors_tests = test.objects.filter(id_doctor =int(id) )
    template = loader.get_template('tests_Data.html')
    context = {"TestsData":doctors_tests}
    return HttpResponse(template.render(context, request))     

# Create your views here.
@login_required 
def R_patient_appointment(request,id):
    patients_appointment = patient_appointment_data.objects.filter(id_patient =int(id) )
    template = loader.get_template('Appointment_Data.html')
    context = {"doctors_appointment_data":patients_appointment}
    return HttpResponse(template.render(context, request))     


def NewPatient(request):
    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            gender = form.cleaned_data.get('gender')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            patient_bill = form.cleaned_data.get('patient_bill')
            patient_record = patient(name=name,age=age,gender=gender,email=email,address=address,phone=phone,patient_bill=patient_bill)
            patient_record.save()
            return redirect('/')

    else:
        form = NewPatientForm()
    context = {
        'form': form
    }
    template = loader.get_template('patient.html')
    return HttpResponse(template.render(context, request))

def Newcomplain(request):
    if request.method == 'POST':
        form = NewcomplainForm(request.POST)
        if form.is_valid():
            complainant = form.cleaned_data.get('complainant')
            complainant_last = form.cleaned_data.get('complainant_last')
            age = form.cleaned_data.get('age')
            reason = form.cleaned_data.get('reason')
            details = form.cleaned_data.get('details')
            message = form.cleaned_data.get('message')
            file = form.cleaned_data.get('file')
            gender = form.cleaned_data.get('gender')
            user_type = form.cleaned_data.get('user_type')
            r_record = complain(complainant=complainant,complainant_last=complainant_last,reason=reason,age=age,details=details,message=message,file=file,gender=gender,user_type=user_type)
            r_record.save()
            return redirect('/')

    else:
        form = NewcomplainForm()
    context = {
        'form': form
    }
    template = loader.get_template('complainsForm.html')
    return HttpResponse(template.render(context, request))


def NewDoctor(request):
    if request.method == 'POST':
        form = NewDoctorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            second_name = form.cleaned_data.get('second_name')
            third_name = form.cleaned_data.get('third_name')
            age = form.cleaned_data.get('age')
            salary = form.cleaned_data.get('salary')
            shift = form.cleaned_data.get('shift')
            gender = form.cleaned_data.get('gender')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            Doctor_record = Doctor( first_name=first_name , second_name=second_name , third_name=third_name , age=age , gender=gender , email=email , address=address , shift=shift , phone=phone , salary=salary)
            Doctor_record.save()
            return redirect('/')

    else:
        form = NewDoctorForm()
    context = {
        'form': form
    }
    template = loader.get_template('doctors.html')
    return HttpResponse(template.render(context, request))

def NewNurse(request):
    if request.method == 'POST':
        form = NewNurseForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            second_name = form.cleaned_data.get('second_name')
            third_name = form.cleaned_data.get('third_name')
            age = form.cleaned_data.get('age')
            salary = form.cleaned_data.get('salary')
            shift = form.cleaned_data.get('shift')
            gender = form.cleaned_data.get('gender')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            Nurse_record = nurse( first_name=first_name , second_name=second_name , third_name=third_name , age=age , gender=gender , email=email , address=address , shift=shift , phone=phone , salary=salary)
            Nurse_record.save()
            return redirect('/')

    else:
        form = NewNurseForm()
    context = {
        'form': form
    }
    template = loader.get_template('nurse.html')
    return HttpResponse(template.render(context, request))    

def NewTest(request):
    if request.method == 'POST':
        form = NewTestForm(request.POST)
        if form.is_valid():
            test_type = form.cleaned_data.get('test_type')
            average_time = form.cleaned_data.get('average_time')
            cost = form.cleaned_data.get('cost')
            id_medical_device = form.cleaned_data.get('id_medical_device')
            id_patient = form.cleaned_data.get('id_patient')
            id_doctor = form.cleaned_data.get('id_doctor')
            # print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            # print(id_doctor)
            Test_record = test( test_type=test_type , average_time=average_time , cost=cost , id_medical_device=id_medical_device , id_patient=id_patient , id_doctor = id_doctor)
            Test_record.save()
            return redirect('/')

    else:
        form = NewTestForm()
    context = {
        'form': form
    }
    template = loader.get_template('add_test.html')
    return HttpResponse(template.render(context, request))        

def NewAppointment(request):
    if request.method == 'POST':
        form = NewAppointmentForm(request.POST)
        if form.is_valid():    
            appointment_place = form.cleaned_data.get('appointment_place')
            appointment_time = form.cleaned_data.get('appointment_time')
            id_doctor = form.cleaned_data.get('id_doctor')
            id_patient = form.cleaned_data.get('id_patient')
            Appointment_record = patient_appointment_data( appointment_place=appointment_place , appointment_time=appointment_time , id_doctor=id_doctor , id_patient=id_patient)
            Appointment_record.save()
            return redirect('/')

    else:
        form = NewAppointmentForm()
    context = {
        'form': form
    }
    template = loader.get_template('add_appointment.html')
    return HttpResponse(template.render(context, request))       

def Newspeciality(request):
    if request.method == 'POST':
        form = NewspecialitytForm(request.POST)
        if form.is_valid():    
            name = form.cleaned_data.get('name')
            id_doctor = form.cleaned_data.get('id_doctor')
            sp_record = Doctors_spiciality( name=name , id_doctor=id_doctor)
            sp_record.save()
            return redirect('/')

    else:
        form = NewspecialitytForm()
    context = {
        'form': form
    }
    template = loader.get_template('add_speciality.html')
    return HttpResponse(template.render(context, request))         

def Newqualification(request):
    if request.method == 'POST':
        form = NewsqualificationtForm(request.POST)
        if form.is_valid():    
            name = form.cleaned_data.get('name')
            id_doctor = form.cleaned_data.get('id_doctor')
            qu_record = Doctors_qualification( name=name , id_doctor=id_doctor)
            qu_record.save()
            return redirect('/')

    else:
        form = NewsqualificationtForm()
    context = {
        'form': form
    }
    template = loader.get_template('add_qualification.html')
    return HttpResponse(template.render(context, request))             


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, '../templates/login.html',
                  context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')