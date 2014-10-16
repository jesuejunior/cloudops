from rest_framework import serializers
from api.models import Server

__author__ = 'jesuejunior'

class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ('id', 'ipaddress', 'system_operational',)

