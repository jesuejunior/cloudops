from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from api.models import Application
from api.serializers.application import ApplicationSerializer

__author__ = 'jesuejunior'


class ApplicationNew(generics.CreateAPIView):

    """
        Cadastrar aplicacoes
    """
    model = Application
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ApplicationSerializer


class ApplicationList(generics.ListAPIView):
    """
        Listar todas aplicacoes cadastradas
    """
    model = Application
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ApplicationSerializer

class ApplicationEdit(generics.RetrieveUpdateAPIView):
    """
        Editar aplicacoes cadastradas
    """
    model = Application
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ApplicationSerializer

class ApplicationDetail(generics.RetrieveAPIView):
    """
        Detalhes da aplicacao selecionada
    """
    model = Application
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ApplicationSerializer

class ApplicationDelete(generics.DestroyAPIView):
    """
        Deletar aplicacao selecionada
    """
    model = Application
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ApplicationSerializer



