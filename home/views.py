from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):

    return render(request, 'home.html')
    # return HttpResponse("Welcome! to the Homepage.")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("Welcome! to the Aboutpage.")
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("Welcome! to the Servicespage.")
def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        contact = Contact(name=name, email=email, mobile=mobile, password=password, date=datetime.today())
        contact.save()
        messages.success(request, 'Form has been submitted!!') 
    return render(request, 'contacts.html')
    # return HttpResponse("Welcome! to the Contactspage.")
def doctor(request):
    return render(request, 'doctor.html')
def patient(request):
    return render(request, 'patient.html')
def guest(request):
    return render(request, 'guest.html')

def doctorsignup(request):
    if request.method =='POST':
        doctorusername = request.POST['doctorusername']
        doctorfname = request.POST['doctorfname']
        doctorlname = request.POST['doctorlname']
        doctormobile = request.POST['doctormobile']
        doctoremail = request.POST['doctoremail']
        registrationnumber = request.POST['registrationnumber']
        specialisation = request.POST['specialisation']
        doctorpassword = request.POST['doctorpassword']
        
        # Check for errorneous inputs
        if not doctorusername.isalnum():
            messages.error(request, "Username should only contain letters and numbers.")
            return redirect('/doctor')

        # Creating the User
        myuser = User.objects.create_user(doctorusername, doctoremail, doctorpassword)
        myuser.first_name = doctorfname
        myuser.last_name = doctorlname
        myuser.save()
        messages.success(request, "Registration Successful!")
        return redirect('/doctor')
    
    else:
        return HttpResponse('404 - Not Found')

def doctorlogin(request):
    if request.method =='POST':
        doctorloginusername = request.POST['doctorloginusername']
        doctorloginpassword = request.POST['doctorloginpassword']

        user = authenticate(username=doctorloginusername, password = doctorloginpassword)

    
        if user is not None:
            login(request, user)
            messages.success(request, "Sucessfully Logged In!")
            return render(request,'doctorlogin.html')
        
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/doctor')


    return render(request, 'doctor.html')

def doctorlogout(request):
    
    logout(request)
    messages.success(request, "Sucessfully Logged Out!")
    return redirect('/doctor')


def patientsignup(request):
    if request.method =='POST':
        patientusername = request.POST['patientusername']
        patientfname = request.POST['patientfname']
        patientlname = request.POST['patientlname']
        patientmobile = request.POST['patientmobile']
        patientemail = request.POST['patientemail']
        patientpassword = request.POST['patientpassword']
       

        # Check for errorneous inputs
        if not patientusername.isalnum():
            messages.error(request, "Username should only contain letters and numbers.")
            return redirect('/patient')

        # Creating the User
        myuser = User.objects.create_user(patientusername, patientemail, patientpassword)
        myuser.first_name = patientfname
        myuser.last_name = patientlname
        myuser.save()
        messages.success(request, "Registration Successful!")
        return redirect('/patient')
    
    else:
        return HttpResponse('404 - Not Found')

def patientlogin(request):
    if request.method =='POST':
        patientloginusername = request.POST['patientloginusername']
        patientloginpassword = request.POST['patientloginpassword']

        user = authenticate(username=patientloginusername, password = patientloginpassword)

       
        if user is not None :
            login(request, user)
            messages.success(request, "Sucessfully Logged In!")
            return render(request,'patientlogin.html')
        
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/patient')
            
    return render(request, 'patient.html')

def patientlogout(request):
    
    logout(request)
    messages.success(request, "Sucessfully Logged Out!")
    return redirect('/patient')