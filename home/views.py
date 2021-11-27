from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .tasks import send_welcome_mail

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:   # if it has already loggedin, redirect it to dashboard
        return redirect('dashboard')
    return render(request, 'home/loginPage1.html')

@login_required(login_url='loginPage')
def dashboard(request):
    username = request.user.username
    stud = Student_table.objects.get(roll_no=username)
    attendance_obj = Tbl_attendance.objects.filter(stud_roll_no=username, semester='5')
    total = {'total':0, 'present':0}
    attendance_data = {}
    for aten_obj in attendance_obj:
        if aten_obj.subject_id.id not in attendance_data:
            attendance_data[aten_obj.subject_id.id] = {
                'name':aten_obj.subject_id.subject_name,
                'present': 0,
                'total': 0
            }
        if aten_obj.attendence=='P':
            attendance_data[aten_obj.subject_id.id]['present'] += 1
            total['present'] += 1
        attendance_data[aten_obj.subject_id.id]['total'] += 1
        total['total'] = total['total'] + 1

    return render(request, 'home/dashboard1.html', {'student':stud, 'attendance':[attendance_data,total]})

def signUp(request):
    if request.method == 'POST':
        # get the entries
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # check for false entries
        try:
            stud = Student_table.objects.get(roll_no=username)
        except:
            messages.error(request, "roll number not found")
            return redirect('signUp')
        if len(username) != 12:    # username must be your roll number
            messages.error(request, "Username must be your roll number")
            return redirect('signUp')
        if email != stud.email:  # should enter the registered email
            messages.error(request, "Enter the mail registered to the college")
            return redirect('signUp')
        if pass1!=pass2:    # passwords should be same
            messages.error(request, "Passwords do not match")
            return redirect('signUp')
        if len(pass1)<8:    # password length should be greater than 7
            messages.error(request, "Password length must be greater than 7")
            return redirect('signUp')
        # create the user and save to database
        try:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.save()
        except:
            messages.error(request,"User already existed")
            return render(request,'home/loginPage1.html')
        send_welcome_mail.delay(email, stud.first_name) # send a welcome mail
        # print("\nuser created")
        messages.success(request, 'Your connectSeek account has been created successfully!')
        return redirect('loginPage')
    else:   
        return render(request,'home/loginPage1.html')

def changePassword(request):
    if request.method == 'POST':
        # get old and new password
        oldpass = request.POST['oldPass']
        newPass = request.POST['newPass']
        username = request.POST['username']
        user = authenticate(username=username, password=oldpass)
        if user is not None:
            user.set_password(newPass)
            messages.success(request, "Password Changed Successfully, Please login back with new password")
            user.save()
        else:
            messages.error(request, "Password Incorrect")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))   # redirects to the page where it has been made to logout


@login_required(login_url='loginPage')
def editProfile(request):
    if request.method == 'POST':
        print("\nin editprofile post request\n")
        username = request.user.username
        stud = Student_table.objects.get(roll_no=username)
        stud.first_name = request.POST['first_name']
        stud.last_name = request.POST['last_name']
        stud.phone = request.POST['phone']
        stud.address = request.POST['address']
        stud.email = request.POST['email']
        stud.save()
        messages.success(request, "Profile Edited Successfully")
        return redirect('dashboard')
    username = request.user.username
    stud = Student_table.objects.get(roll_no=username)
    return render(request, 'home/editProfile.html', {'stud':stud})


@login_required(login_url='loginPage')
def assignment(request):
    username = request.user.username
    stud = Student_table.objects.get(roll_no=username)
    assignments = assignment_details.filter()
    return render(request, 'home/assignment.html', {'student':stud})

@login_required(login_url='loginPage')
def feePayment(request):
    username = request.user.username
    stud = Student_table.objects.get(roll_no=username)
    subjects = Subject_table.filter(semester=stud.semester, field=stud.program)
    
    return render(request, 'home/fees.html', {'student':stud})

@login_required(login_url='loginPage')
def knowledgeCenter(request):
    username = request.user.username
    stud = Student_table.objects.get(roll_no=username)
    return render(request, 'home/knowledgeCenter.html', {'student':stud})


# Authentication API's

def handleLogin(request):
    if request.method == 'POST':
        # get the username and password
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('loginPage')
    raise Http404("Invalid Access")

def handleLogout(request):
    logout(request)
    return redirect('loginPage')