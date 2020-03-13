from django.shortcuts import render ,redirect
from .models import Profile , Posts ,friend
from django.contrib.auth.models import User
from django.http import HttpResponse


# The password for the user is rohit2332
def profile_page(request,id):
	login = 0
	if (request.user.is_authenticated):
		posts 	= Posts.objects.filter(user = request.user)
		friends = friend.objects.filter(my_detail = request.user)
		return render(request,'profile.html', {'posts':posts,'friends':friends})
	else:
		return redirect('/login')



def display(request,id):
	try:
		user 					= 	User.objects.get(id= id)
	except:
		return HttpResponse('<center><h1>trying to hack ? You missed it then</h1></center>')
	data 					=   {}
	try :
		post 				= 	Posts.objects.filter(user = user)
		data['posts'] 		= 	post
	except:
		data['posts'] 		= 	'No Posts'

	try:
		p 					=	Profile.objects.get(user = user)
		data['profile'] 	= 	p
	except:
		data['profile'] 	= 	'user Doesnot exists'
	try:
		f 	 				= 	friend.objects.filter(my_detail = user)
		data['friends'] 	=	f
	except:
		data['friends']		= 	'No friends'
	return render(request,'display_profile.html',data)


def all_people(request):
	p = Profile.objects.filter()
	return render(request,'all_people.html',{'profiles':p})

def saving_post(request):
	if (request.method == 'POST'):
		p = Posts()
		p.user 			=	request.user
		p.content_type  =	request.POST['content_type']
		p.content 	 	=	request.POST['content']
		p.no_of_likes 	= 	0
		p.no_of_comments = 0
		p.save()
		return redirect('/profile/'+str(request.user.id))
	else:
		return HttpResponse("something is wrong!!")
def test(request):
	return render(request,'testbase.html')