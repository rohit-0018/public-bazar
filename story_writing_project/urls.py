
from django.contrib import admin
from django.urls import path
from core import views
from user_management.views import profile_page , display , all_people ,test , saving_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.mainpage),
    path('logout/',views.user_logout),
    path('signup/',views.mainpage),
    path('profile/<int:id>',profile_page),
    path('',views.mainpage),
    path('ajaxreq/<slug:username>', views.ajax_for_login),
    path('ajax_check_u/<slug:uname>',views.ajax_check_uname_exist),
    path('ajax_check_e/',views.ajax_check_email_exist),
    path('display/<int:id>',display),
    path('exploring/',all_people),
    path('test/',test) ,
    path('savepost',saving_post)
]

