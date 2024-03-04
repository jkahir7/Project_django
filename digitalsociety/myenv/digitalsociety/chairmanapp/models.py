from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique = True,max_length = 30)
    password = models.CharField(max_length = 30)
    role = models.CharField(max_length=10)
    otp = models.IntegerField(default = 456)
    is_active = models.BooleanField(default = True)
    is_verify = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def __str__(self) -> str:
     return self.email

class chairman(models.Model):
    userid = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    firstname = models.CharField(max_length = 20,null=True)
    lastname = models.CharField(max_length = 20,null=True)
    contactno = models.CharField(max_length = 20,null = True)
    houseno = models.CharField(max_length = 8,null=True)
    pic=models.FileField(upload_to='media/images/',default='default.jpeg')

    def __str__(self) -> str:
       return self.firstname


class member(models.Model):
    userid = models.ForeignKey(User,on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    contactno = models.CharField(max_length = 20,null = True)
    houseno = models.CharField(max_length = 8)
    vehicle_details = models.CharField(max_length = 20,null=True)
    occupation = models.CharField(max_length = 20,null=True)
    no_familymembers = models.CharField(max_length = 20,null=True)
    job_address = models.CharField(max_length = 20,null=True)
    old_city = models.CharField(max_length=20,null=True)
    blood_grp = models.CharField(max_length = 20,null=True)
    birthdate = models.DateField(null=True)
    joining_date = models.DateTimeField(auto_now_add=True,blank=False)
    pic=models.FileField(upload_to='media/images/',default='default.jpeg')

class notice(models.Model):
    userid = models.ForeignKey(User,on_delete = models.CASCADE)
    title=models.CharField(max_length=50)
    discription=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)


class student(models.Model):
   name = models.CharField(max_length=20)
   subject = models.CharField(max_length=20)