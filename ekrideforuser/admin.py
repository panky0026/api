from django.contrib import admin

# Register your models here.
from django.contrib import admin

from ekrideforuser.models import Registrationform

# Register your models here


class appAdmin(admin.ModelAdmin):
        
    list_display=['Enter_Name','Create_Password','Enter_Email','Enter_Address','Enter_Mobile_Number']

admin.site.register(Registrationform,appAdmin)