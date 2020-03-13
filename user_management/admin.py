from django.contrib import admin
from user_management.models import Profile , Posts ,friend , friend_request

admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(friend_request)
admin.site.register(friend)