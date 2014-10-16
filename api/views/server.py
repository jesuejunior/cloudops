from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from api.models import Server
from api.serializers.server import ServerSerializer

__author__ = 'jesuejunior'

class ServerNew(generics.CreateAPIView):
    """
        Endpoint para criar novo servidor
    """
    model = Server
    serializer_class = ServerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class ServerList(generics.ListAPIView):
    """
    Endpoint para listar todos os servidores
    """
    model = Server
    serializer_class = ServerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)