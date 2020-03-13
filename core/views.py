from django.shortcuts import render ,redirect
from django.contrib.auth import login , authenticate , logout
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def user_login(request):

	if (request.method == 'POST'):
		u_name 		 =	request.POST['username']
		password	=	request.POST['password']	
		user 		=	authenticate(request,username = u_name , password = password)
		if user:
			login(request,user)
			return	1 											#returning true if details are correct
		else:
			return 0											#returning false if logged in 
	

def user_logout(request):
	user  = request.user
	logout(request)
	return redirect('/')



#...

def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            u_name 	=	request.POST['username']
            user 	=	User.objects.get(username =u_name)
            login(request,user)
            print("you are logged in")
            return 1
        else:
        	#cal_errors(request)
        	print("wrong creditionals")
        	return 0
 

def mainpage(request):
	if (request.user.is_authenticated):
		return redirect('/profile/'+str(request.user.id))
		
	if (request.method=='GET'):
		if (request.user.is_authenticated):
			return redirect('/home')
		form = CustomUserCreationForm()
		return render(request,'mainpage.html', {'form':form})
	
	elif (request.method == 'POST'):
		if('login' in request.POST):							# If login button is pressed
			login_status = user_login(request)
			
			if login_status == True:
				return	redirect('/profile/'+str(request.user.id))
			else:
				#return error message that wrong password
				return render(request,'mainpage.html',{'l_p_err':"wrong password"})
		
		elif('signup' in request.POST):							# If signup button is pressed
			status = user_signup(request)						#This is a function which handels signup logic for us written above
			'''
			Here the problem is that i am not able to 
			show the errors of the form which form is generating
			1) I can do u_name and email by ajax
			2) I can do pass using js	which is not a good idea because browser will encode it i guess



			'''
			if (status == 1):
				return redirect('/home')						#redirecting to the profile page because the user is signed inn
			elif(status==0):
				psw1 = request.POST.get('password1')
				psw2 = request.POST.get('password2')
				if (psw1 !=psw2):
					msg = "password did'nt match"
					return render(request,'mainpage.html',{'p_err':msg})
				else:
					gmsg = "Details were not right"
					return render(request,'mainpage.html',{'general_err':gmsg})
		else:
			return HttpResponse("some thing went wrong!")		#This is ain't gonna happen


#	This view handels the ajax request created by the user
@csrf_exempt
def ajax_for_login(request,username):
	print("the usr name is ",username)
	try:
		u 	= User.objects.get(username = username)
		return HttpResponse(1)
	except:
		return HttpResponse(0)


@csrf_exempt
def ajax_check_uname_exist(request,uname):
	try:
		u = User.objects.get(username = uname)
		return HttpResponse(1)
	except:
		return HttpResponse(0)





@csrf_exempt
def ajax_check_email_exist(request):
	try:
		email = request.body.decode()
		status = User.objects.get(email = email)
		return HttpResponse(1)
	except:
		print("try didnt ran")
		return HttpResponse(0)