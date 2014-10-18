from rest_framework import serializers
from api.models import Server

__author__ = 'jesuejunior'

class ServerSerializer(serializers.ModelSerializer):
    applications = serializers.RelatedField(many=True, read_only=False)

    class Meta:
        model = Server
        fields = ('id', 'name', 'ipaddress', 'system_operational', 'applications')


