from django.shortcuts import render

from . import serializers
from . import models
from . import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# Create your views here.

class Login_Viewset(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken().post(request)


class User_Profile_Viewset(viewsets.ModelViewSet):

     serializer_class = serializers.User_Profile_Serializer
     queryset = models.User_Profile.objects.all()
     authentication_classes = (TokenAuthentication,)
     permission_classes = (permissions.User_Profiles_Management_Permission,IsAuthenticated,)


class Project_Viewset(viewsets.ModelViewSet):

    serializer_class = serializers.Project_Serializer
    queryset = models.Project.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.Projects_Management_Permission,)


class Report_Viewset(viewsets.ModelViewSet):

    serializer_class = serializers.Report_Serializer
    queryset = models.Report.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.Report_Management_Permission,)


class Investment_Viewset(viewsets.ModelViewSet):

    serializer_class = serializers.Investment_Serializer
    queryset = models.Investment.objects.all()
