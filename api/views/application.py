# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.models import Application
from api.serializers.application import ApplicationSerializer


__author__ = 'jesuejunior'

class BaseApplicationView():
    model = Application
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ApplicationSerializer

class ApplicationNew(BaseApplicationView, generics.CreateAPIView):
    u"""
        Cadastrar aplicações
    """

class ApplicationList(BaseApplicationView, generics.ListAPIView):
    u"""
        Listar todas as aplicações cadastradas.
    """

class ApplicationEdit(BaseApplicationView, generics.RetrieveUpdateAPIView):
    u"""
        Editar aplicações cadastradas
    """

class ApplicationDetail(BaseApplicationView, generics.RetrieveAPIView):
    u"""
        Detalhes da aplicação selecionada.
    """

class ApplicationDelete(BaseApplicationView, generics.DestroyAPIView):
    u"""
        Deletar aplicação selecionada.
    """




