from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
import random
from django.urls import reverse
from .utils import *
"""
get() : it will return object

-> it will return only single object
-> it will throw exception when it will return multiple object
-> if condition not match it will throw exception
"""
# Create your views here.
def login(request):
    if "email" in request.session:
        print("----->>>>>>",request.session['email'])
        uid = User.objects.get(email = request.session['email'])
        print(uid) 
        cid = chairman.objects.get(userid=uid)
        mcount = member.objects.all().count()

        context = {
            'uid' : uid,
            'cid' : cid,
            'mcount':mcount,
         }
        return render(request,"chairmanapp/index.html",context)
    else:
        return render(request,"chairmanapp/login.html")

def login_evalute(request):
    if "email" in request.session:
       return HttpResponseRedirect(reverse("loginpage"))
    else:
 
        try:
            print("=========== this function is called")
            email_var = request.POST["email"]
            password_var = request.POST["password"]
            print("======>> email : ",email_var)
            print("======>> password : ",password_var)
            # ORM : object relational mapper
            uid = User.objects.get(email = email_var , password = password_var)
            print("-------------->> uid : ",uid)
            print("=====>> role : ",uid.role)
            print("======>>is active : ",uid.is_active)
        
            if uid.role=="chairman":
                cid = chairman.objects.get(userid=uid)
                print("firstname = ",cid.firstname)
                # session management
                request.session['email'] = email_var
                context = {

                    "udi":uid,
                    "cid":cid,

                }
                print("----> email ",uid.email)
                print("----> password",uid.password)
                return render(request,"chairmanapp/index.html",context)

            else:
                pass
            return render(request,"chairmanapp/login.html")

        except Exception as e:
            print("==> e : ",e)
            e_msg="invalid email or password"
            print("====>>> emsg",e_msg)
            return render(request,"chairmanapp/login.html",{"e_msg":e_msg})

def logout(request):
    if "email" in request.session:
        del request.session["email"]
        return HttpResponseRedirect(reverse("loginpage"))
    else:
       return HttpResponseRedirect(reverse("loginpage"))

def chairman_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email']) 
        cid = chairman.objects.get(userid=uid)
        context = {
            'uid' : uid,
            'cid' : cid,
         }
        return render(request,"chairmanapp/profile.html",context)
    else:
        return render(request,"chairmanapp/login.html")

def chairman_change_password(request):
    if request.POST:    
        email = request.session['email']
        currentpassword = request.POST['currentpassword']
        newpassword = request.POST['newpassword']
        uid = User.objects.get(email=email)
        if uid:
            if uid.password == currentpassword:
                uid.password = newpassword
                uid.save()
                del request.session["email"]
                s_msg = "successfully password change"
                return render(request,"chairmanapp/login.html",{'s_msg':s_msg})
            else:
                pass

        else:
            pass 

def chairman_update_profile(request):
    if request.POST:
        uid = User.objects.get(email=request.session['email'])
        cid = chairman.objects.get(userid=uid)
        cid.firstname = request.POST['firstname']
        cid.lastname = request.POST['lastname']
        cid.houseno = request.POST['houseno']
        cid.contactno = request.POST['contactno']

        if "profilepic" in request.FILES:
            picture = request.FILES['profilepic']
            cid.pic = picture
            cid.save()
        cid.save()

        context = {
            'uid' : uid,
            'cid' : cid,
         }
        return render(request,"chairmanapp/profile.html",context)
    
def add_member(request):
    if request.POST:
        uid = User.objects.get(email = request.session['email']) 
        cid = chairman.objects.get(userid=uid)
        context = {
            'uid' : uid,
            'cid' : cid,
        }
        if "mid" in request.POST:
            mid=member.objects.get(id = request.POST('id'))
            return render(request,"chairmanapp/add_member.html",context)
        else:
            email = request.POST['email']
            contactno = request.POST['contactno']
            l1 = ["as12d","as13d","as14d","as15d","as62d","as17d","as652d"]
            password = random.choice(l1)+email[3:6]+contactno[4:6]
            firstname = request.POST['firstname'],

            muid = User.objects.create(email=email,password=password,role="member")
            mid = member.objects.create(userid=muid,
                                        firstname = request.POST['firstname'],
                                        lastname = request.POST['lastname'],
                                        contactno = request.POST['contactno'],
                                        houseno = request.POST['houseno'],
                                        old_city=request.POST['old_city'],
                                        vehicle_details = request.POST['vehicle_details'],
                                        occupation = request.POST['occupation'],
                                        no_familymembers = request.POST['no_familymembers'],
                                        job_address = request.POST['job_address'],
                                        blood_grp = request.POST['blood_grp'],
                                        birthdate = request.POST['birthdate'])
                                                            
            mysendmail("welcome","mymailtemplate",email,{"name":firstname ,"password":password})
            return HttpResponseRedirect(reverse("all-member"))
    else:   
        if "email" in request.session:
            uid = User.objects.get(email = request.session['email']) 
            cid = chairman.objects.get(userid=uid)
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/add_member.html",context)
        else:
            return render(request,"chairmanapp/login.html")
        
def all_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email']) 
        cid = chairman.objects.get(userid=uid)
        mall = member.objects.all()

        context = {
            'uid' : uid,
            'cid' : cid,
            'mall': mall,
        }
        return render(request,"chairmanapp/members.html",context)
    
def cmember_profile(request,pk):
     if "email" in request.session:
        uid = User.objects.get(email = request.session['email']) 
        cid = chairman.objects.get(userid=uid)
        mid=member.objects.get(id=pk)
        mall = member.objects.all()
        
        context = {
            'uid' : uid,
            'cid' : cid,
            'mid': mid,
            'mall': mall,
        }
        return render(request,"chairmanapp/cmember_profile.html",context)

def cmember_edit(request,pk):
     if "email" in request.session:
        uid = User.objects.get(email = request.session['email']) 
        cid = chairman.objects.get(userid=uid)
        mid=member.objects.get(id=pk)
        context = {
            'uid' : uid,
            'cid' : cid,
            'mid': mid}
        return render(request,"chairmanapp/add_member.html",context)


def cmember_delete(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email']) 
        cid = chairman.objects.get(userid=uid)
        mid=member.objects.get(id=pk)

        mid.delete()
        return HttpResponseRedirect(reverse("all-member"))

def add_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email']) 
        cid = chairman.objects.get(userid=uid)
        if request.POST:
            nid=notice.objects.create(userid=uid,
                                      title=request.POST['notice_title'],
                                       discription=request.POST['notice_discription'])
                                   
            context = {
                'uid' : uid,
                'cid' : cid,
            }
            return render(request,"chairmanapp/add_notice.html",context)
        else:
            context = {
                    'uid' : uid,
                    'cid' : cid,
                }
            return render(request,"chairmanapp/add_notice.html",context)
    
def forgot_password(request):
    if request.POST:
        email = request.POST['email']
        uid = User.objects.get(email = email)
        otp=random.randint(1111,9999)
        uid.otp=otp
        uid.save()
        mysendmail=('forgot password','mymailtemplateotp',email,{'otp':otp})
        return render(request,"chairmanapp/changepassword.html",{'email':email})

    else:
        return render(request,"chairmanapp/forgotpassword.html")


def change_password(request):
    if request.POST:
        email = request.POST['email']
        password =  request.POST['password']
        otp = request.POST['otp']
        confirmpassword = request.POST['confirmpassword']

        uid = User.objects.get(email = email)
        if otp == str(uid.otp):
            if password == confirmpassword:
                uid.password = password
                uid.save()
                return render(request,"chairmanapp/login.html")
            
def all_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email']) 
        cid = chairman.objects.get(userid=uid)
        mall = notice.objects.all()

        context = {
            'uid' : uid,
            'cid' : cid,
            'mall': mall,
        }
        return render(request,"chairmanapp/allnotice.html",context)
    


def ajax_index(request) :
    return render(request,"chairmanapp/ajax_index.html")

def adddatapage(request):
    print("============================INSIDE THE PYTHON VIEWS FILE ")

    print(request.POST["name"])
    sid = student.objects.create(name = request.POST["name"],
                                 subject = request.POST["subject"],)