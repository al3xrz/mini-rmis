from rest_framework import serializers
from .models import *
from geo.models import *



class MunicipalitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Municipality
        fields = ('id' , 'name')


class LocalitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    municipality = MunicipalitySerializer()
    class Meta:
        model = Locality
        fields = ('id' , 'name', 'municipality')



class PatientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    locality = LocalitySerializer()
    class Meta:
        model = Patient
        fields = ('id' , 'name', 'birthdate', 'locality',)
