from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user			=	models.OneToOneField(User,on_delete = models.CASCADE)
	first_name		=	models.CharField(max_length = 30)
	middle_name		=	models.CharField(max_length = 30,blank = True)
	last_name		=	models.CharField(max_length = 30,blank = True)
	gender			=	models.CharField(max_length = 10)
	profile_pic 	=	models.ImageField(blank= True)
	cover_pic		=	models.ImageField(blank = True)
	date_of_birth	=	models.DateField()
	description		=	models.TextField(blank = True ,default="no des")  #blank = ture has not been migrated
	#verified 		=	models.BooleanField(blank=True)

class Posts(models.Model):
	user 			= 	models.ForeignKey(User,on_delete = models.CASCADE)
	content_type 	=	models.CharField(max_length=50 ,blank = True)				# This will be the caption or the heading of any post
	content 		=	models.TextField()
	# created_at 		=	models.DateTimeField(auto_now_add = True ,default = 0)
	# updated_at		=	models.DateTimeField(auto_now_add = True ,default = 0)
	post_image      =	models.ImageField(blank = True)
	no_of_likes		=	models.IntegerField(blank= True)
	no_of_comments	=	models.IntegerField(blank = True)


class friend_request(models.Model):
	me 				=	models.ForeignKey(User,on_delete = models.CASCADE ,related_name = 'my_self')
	sender 			=	models.ForeignKey(User,on_delete = models.CASCADE ,related_name = 'sender')
	status			=	models.BooleanField(default = False)

class friend(models.Model):
	my_detail 		=	models.ForeignKey(User,on_delete = models.CASCADE,related_name='my_detail')
	friend 			=	models.ForeignKey(User,on_delete = models.CASCADE,related_name='friend')





