"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.chat_home,name='chat_home'),
    path('signup/', views.signup, name='signup'),
    path('start_chat/<str:username>/',views.start_chat,name='start_chat'),
    path('chat/received/<str:username>/', views.receive_chat, name='receive_chat'),
    path('send_chat/',views.send_chat,name='send_chat')
    ]
    #path('login/', views.login, name='login'),
    #path('account/', views.account, name='account'),
   # path('logout/', views.logout, name='logout'),
   # path('job_post/', views.job_post, name='job_post'),
#    path('job_details/', views.job_details, name='job_details'),
   # path('search/', views.search, name='search'),
   # path('profile/', views.profile, name='profile'),
    #path('edit_job/', views.edit_job, name='edit_job'),
    #path('delete/', views.delete, name='delete'),
   # path('about/', views.about, name='about'),
  #  path('contact/', views.contact, name='contact'),
    #path('activity/', views.activity, name='activity'),
   # path('delete_account/', views.delete_account, name='delete_account'),
    #path('forgot/', views.forgot, name='forgot_password'),
    #path('reset/', views.reset, name='reset_password'),
   # path('chat/', views.chat_home, name='chat_home'),
  #  path('update_profile/', views.update_profile, name='update_profile'),
  #  path('chat_search/', views.chat_search, name='chat_search'),
 #   path('chat_get_masage/', views.chat_get_masage, name='chat_get_masage'),
   # path('chat_send_masage/', views.chat_send_masage, name='chat_send_masage'),

