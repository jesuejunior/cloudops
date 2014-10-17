# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.models import Server
from api.serializers.server import ServerSerializer


__author__ = 'jesuejunior'

class BaseServerView():
    model = Server
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ServerSerializer

class ServerNew(BaseServerView, generics.CreateAPIView):
    u"""
         Cadastrar novo servidor.
    """

class ServerList(BaseServerView, generics.ListAPIView):
    u"""
        Listar todos os servidores.
    """

class ServerEdit(BaseServerView, generics.RetrieveUpdateAPIView):
    u"""
        Editar servidores cadastradas
    """

class ServerDetail(BaseServerView, generics.RetrieveAPIView):
    u"""
        Detalhes do servidor selecionado.
    """

class ServerDelete(BaseServerView, generics.DestroyAPIView):
    u"""
        Deletar servidor selecionado.
    """
