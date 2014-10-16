from rest_framework import serializers
from api.models import Application

__author__ = 'jesuejunior'

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ('id', 'name', 'description',)


