"""
URL configuration for digitalsociety project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='loginpage'),
    path('login-evalute/',views.login_evalute,name='login-evalute'),
    path('logout/', views.logout,name='logout'),
    path('chairman-profile/', views.chairman_profile,name='chairman-profile'),
    path('chairman-change-password/', views.chairman_change_password,name='chairman-change-password'),
    path('chairman-update-profile/', views.chairman_update_profile,name='chairman-update-profile'),
    path("add-member/",views.add_member,name="add-member"), 
    path("all-member/",views.all_member,name="all-member"),
    path('cmember-profile/<int:pk>',views.cmember_profile,name="cmember-profile"),
    path('cmember-edit/<int:pk>',views.cmember_edit,name="cmember-edit"),
    path('cmember-delete/<int:pk>',views.cmember_delete,name="cmember-delete"),
    path('add-notice',views.add_notice,name="add-notice"),
    path('forgot-password/',views.forgot_password,name="forgot-password"),
    path('change-password/',views.change_password,name="change-password"),
    path("all-notice/",views.all_notice,name="all-notice"),
    path('ajax-index',views.ajax_index,name="ajax-index"),
    path('adddatapage',views.adddatapage,name="adddatapage")




]
