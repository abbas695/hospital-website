from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import patient ,Doctor ,Doctors_qualification,complain ,nurse , test ,patient_appointment_data ,Doctors_spiciality ,User


class NewPatientForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    CHOICES = [('male', 'Male'),
               ('female', 'Female'),
               ('prefer not to say', 'prefer not to say')]
    gender = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': ''}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)

    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)

    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))

    patient_bill = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)

    medical_report = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    class Meta:
        model = patient
        fields = ('name', 'age', 'gender', 'email',
                  'address', 'phone', 'patient_bill', 'medical_report')

class NewDoctorForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    second_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    third_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)        
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    CHOICES = [('male', 'Male'),
               ('female', 'Female'),
               ('prefer not to say', 'prefer not to say')]
    gender = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': ''}))
    salary = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
    shift = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=False)
    class Meta:
        model = Doctor
        fields = ('first_name', 'second_name', 'third_name', 'age',
                  'gender', 'salary', 'email', 'phone','address' , 'shift')

class NewNurseForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    second_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    third_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)        
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    CHOICES = [('male', 'Male'),
               ('female', 'Female'),
               ('prefer not to say', 'prefer not to say')]
    gender = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': ''}))
    salary = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
    shift = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=False)
    class Meta:
        model = nurse
        fields = ('first_name', 'second_name', 'third_name', 'age',
                  'gender', 'salary', 'email', 'phone','address' , 'shift')                  

class NewTestForm(forms.ModelForm):
    test_type = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)      
    average_time = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    cost = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    id_medical_device = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    id_patient = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True) 
    id_doctor = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True) 
    class Meta:
        model = test
        fields = ('test_type', 'cost', 'average_time', 'id_medical_device','id_patient','id_doctor')                

class NewAppointmentForm(forms.ModelForm):
    appointment_place = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)      
    appointment_time =forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    id_doctor = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    id_patient = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)        
    class Meta:
        model = patient_appointment_data
        fields = ('appointment_place', 'appointment_time', 'id_doctor','id_patient')         

class NewspecialitytForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)      
    id_doctor = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)       
    class Meta:
        model = Doctors_spiciality
        fields = ('name', 'id_doctor')           

class NewsqualificationtForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)      
    id_doctor = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)       
    class Meta:
        model = Doctors_qualification
        fields = ('name', 'id_doctor')   

class NewcomplainForm(forms.ModelForm):
    complainant = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    complainant_last = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)      
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    CHOICES = [('male', 'Male'),
               ('female', 'Female'),
               ('prefer not to say', 'prefer not to say')]
    gender = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': ''}))
    CHOICES2 = [('Employee', 'Employee'),
               ('customer', 'customer'),]
    user_type = forms.ChoiceField(
        choices=CHOICES2, widget=forms.RadioSelect(attrs={'class': ''}))
    reason = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    details = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control form-control-lg'}), required=True)        
    file = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control form-control-lg'}), required=False)     
    class Meta:
        model = complain
        fields = ('complainant', 'complainant_last','age', 'gender', 'reason', 'details', 'message','user_type' , 'file')            




class PatientSignUpForm(UserCreationForm): 
    name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)    
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    CHOICES = [('male', 'Male'),
               ('female', 'Female'),
               ('prefer not to say', 'prefer not to say')]
    gender = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': ''}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)

    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)

    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))

    patient_bill = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)

    medical_report = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control form-control-lg'}), required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        #fields = '__all__'
        fields = UserCreationForm.Meta.fields + \
            ('name', 'age', 'gender', 'phone',
            'address', 'patient_bill', 'medical_report')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient_data = patient.objects.create(
            user=user, name=self.cleaned_data.get('name'), age=self.cleaned_data.get('age'),
            gender=self.cleaned_data.get('gender'), email=self.cleaned_data.get('email'), phone=self.cleaned_data.get('phone'),
            address=self.cleaned_data.get('address'), patient_bill=self.cleaned_data.get('patient_bill'),
            medical_report=self.cleaned_data.get('medical_report'))
        patient_data.save()
        return user


class DoctorSignUpForm(UserCreationForm): 
    first_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True) 
    second_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    third_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
           
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    CHOICES = [('male', 'Male'),
               ('female', 'Female'),
               ('prefer not to say', 'prefer not to say')]
    gender = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': ''}))
    salary = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
    shift = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        #fields = '__all__'
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'second_name', 'third_name', 'age',
            'gender', 'salary', 'email','address','phone','shift')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor_data = Doctor.objects.create(
            user=user, first_name=self.cleaned_data.get('first_name'), second_name=self.cleaned_data.get('second_name'),
            third_name=self.cleaned_data.get('third_name'), age=self.cleaned_data.get('age'), gender=self.cleaned_data.get('gender'),
            salary=self.cleaned_data.get('salary'), email=self.cleaned_data.get('email'),phone=self.cleaned_data.get('phone'),shift=self.cleaned_data.get('shift'),
            address=self.cleaned_data.get('address'))
        doctor_data.save()
        return user

class NurseSignUpForm(UserCreationForm): 
    first_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True) 
    second_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    third_name= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
           
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    CHOICES = [('male', 'Male'),
               ('female', 'Female'),
               ('prefer not to say', 'prefer not to say')]
    gender = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': ''}))
    salary = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
    shift = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}), required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        #fields = '__all__'
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'second_name', 'third_name', 'age',
            'gender', 'salary', 'email','address','phone','shift')            

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_nurse = True
        user.save()
        nurse_data = nurse.objects.create(
            user=user, first_name=self.cleaned_data.get('first_name'), second_name=self.cleaned_data.get('second_name'),
            third_name=self.cleaned_data.get('third_name'), age=self.cleaned_data.get('age'), gender=self.cleaned_data.get('gender'),
            salary=self.cleaned_data.get('salary'), email=self.cleaned_data.get('email'),phone=self.cleaned_data.get('phone'),shift=self.cleaned_data.get('shift'),
            address=self.cleaned_data.get('address'))
        nurse_data.save()
        return user
                