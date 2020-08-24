from . import models
from rest_framework import permissions



class User_Profiles_Management_Permission(permissions.BasePermission):

    def has_object_permission(self , request , view , obj):
        if request.user.id == obj.id:
            return True

class Projects_Management_Permission(permissions.BasePermission):

    def has_object_permission(self , request , view , obj):
        if obj.producer.id == request.user.id:
            return True

class Report_Management_Permission(permissions.BasePermission):

    def has_object_permission(self , request , view , obj):
        if obj.reporter.id == request.user.id:
            return True
