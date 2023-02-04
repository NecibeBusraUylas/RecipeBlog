#Serializers in Django REST Framework are responsible for converting objects(querysets and model instances) into data types understandable by JS 
#and front-end frameworks. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first 
#validating the incoming data.

from rest_framework import serializers
from .models import category,blog

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
        
class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = '__all__'