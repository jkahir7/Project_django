from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(chairman)
admin.site.register(member)
admin.site.register(notice)
admin.site.register(student)