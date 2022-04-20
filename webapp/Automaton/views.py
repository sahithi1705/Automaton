from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib import auth
from accounts.models import Account
from django.core.mail import send_mail
from Automaton.models import Bookings
import random,math
to_list=[0]*1
email,first_name,last_name,phone,vehicle,address,new_password='','','','','','',''
def index(request):
	return render(request,'index.html',{})
def info(request):
	return render(request,'info.html',{})
def register(request):
		if request.method=='POST':
			first_name=request.POST['first_name']
			last_name=request.POST['last_name']
			username=request.POST['username']
			password=request.POST['password']
			email=request.POST['email']
			confirm=request.POST['confirm']
			if first_name=='' or last_name=='' or username=='' or password=='' or email=='' or confirm=='':
				messages.info(request,'Please Enter valid details')
				return redirect('register')
			if password==confirm:
				try:
					user=Account.objects.get(username=username)
					messages.info(request,"Username already taken")
					return redirect('register')
				except Account.DoesNotExist:
					try:
						user=Account.objects.get(email=email)
						messages.info(request,"The Email id is already registered")
						return redirect('register')
					except Account.DoesNotExist:
						user=Account.objects.create_user(username=username,First_name=first_name,Last_name=last_name,password=password,email=email)
						user.save()
						return redirect('/')
			else:
				messages.info(request,"Password not matched")
		else:
			return render(request,'register.html',{})

def login(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		user=auth.authenticate(email=email,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,"Invalid username/password")
			return redirect('login')
	else:
		return render(request,'login.html',{})
def logout(request):
	auth.logout(request)
	return redirect('/')
def profile(request):
	return render(request,'profile.html',{})
def forgot(request):
	if request.method=='POST':
		global email
		global new_password
		email=request.POST['email']
		new_password=request.POST['new_password']
		otp=generateotp()
		to_list[0]=email
		request.session['otp']=otp
		return render(request,'otp_verify2.html',{})
		
	return render(request,'forgot.html',{})
def generateotp():
	digits='0123456789'
	otp=''
	for i in range(4):
		otp+=digits[math.floor(random.random()*10)]
	subject="Automaton"
	message="OTP is "+otp
	from_mail=settings.EMAIL_HOST_USER
	send_mail(subject,message,from_mail,to_list,fail_silently=False)
	return otp
def otp_verify(request):
	otp2=request.session['otp']
	if request.method=='POST':
		otp1=request.POST['otp']
		if otp1==otp2:
			booking=Bookings(Phone=phone,First_name=first_name,Last_name=last_name,Vehicle=vehicle,Address=address)
			booking.save()
			return render(request,'booked.html')
		else:
			messages.info(request,"Invalid OTP")
			return redirect('register')
def book(request):
	if request.method=='POST':
		global email,first_name,last_name,vehicle,address,phone
		email=request.POST['email']
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		vehicle=request.POST['Vehicle']
		address=request.POST['Address']
		phone=request.POST['phone']
		if email=='' or first_name=='' or last_name=='' or vehicle=='Vehicle' or address=='':
			messages.info(request,"Please Enter valid details")
			return redirect('book')
		to_list[0]=email
		otp2=generateotp()
		request.session['otp']=otp2
		return render(request,'otp_verify.html')
	else:
		return render(request,'book.html',{})
def services(request):
	return render(request,'services.html',{})
def otp_verify2(request):
	if request.method=='POST':
		otp2=request.POST['otp']		
		otp1=request.session['otp']
		if otp1==otp2:
			try:
				user=Account.objects.get(email=email)
				user.set_password(new_password)
				user.save()
				return render(request,'password_change.html',{})
			except Account.DoesNotExist:
				messages.info(request,"Account with that email does not exist")
				return redirect('otp_verify2')
		else:
			messages.info(request,"Invalid OTP")
			return redirect('otp_verify2')
	return render(request,'otp_verify2.html',{})