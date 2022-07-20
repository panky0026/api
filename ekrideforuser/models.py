from django.db import models

# Create your models here.
# Create your models here.

# Create your models here.


class Registrationform(models.Model):
    Enter_Name = models.CharField(max_length = 25 ,null=True)
    Create_Password = models.CharField(max_length = 8 ,null=True)
    Enter_Email = models.CharField(max_length = 50 ,null=True)
    Enter_Address = models.CharField(max_length = 500 ,null=True)
    Enter_Mobile_Number= models.CharField(max_length = 10 ,null=True)
    