from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets 

from ekrideforuser.serializer import RegistrationformSerializer
 
# import local data
from .models import Registrationform
 
# create a viewset
class RegistrationformViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Registrationform.objects.all()
     
    # specify serializer to be used
    serializer_class = RegistrationformSerializer