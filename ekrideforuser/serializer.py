
# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import Registrationform
 
# Create a model serializer
class RegistrationformSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Registrationform
        fields = ('Enter_Name','Create_Password','Enter_Email','Enter_Address','Enter_Mobile_Number')