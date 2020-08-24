from . import models
from rest_framework import serializers



class User_Profile_Serializer(serializers.ModelSerializer):

    class Meta:
        model = models.User_Profile
        fields = ('id','email','name','family_name','role','password','investments','producing_projects','reports')
        extra_kwargs = {'password':{'write_only' : True} , 'investments' : {'read_only' : True} , 'producing_projects' : {'read_only' : True} , 'reports' : {'read_only' : True}}

    def create(self , validated_data):
            user = models.User_Profile(
            email = validated_data['email'],
            name = validated_data['name'],
            family_name = validated_data['family_name'],
            role = validated_data['role']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

    def update(self , instance , validated_data):

             instance.email = validated_data['email']
             instance.name = validated_data['name']
             instance.family_name = validated_data['family_name']
             instance.role = validated_data['role']
             instance.set_password(validated_data['password'])
             instance.save()
             return instance

class Project_Serializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = ('id','title','topic','description','estimated_time','needed_money','location','producer','investments')
        extra_kwargs = {'investments':{'read_only' : True}}

class Report_Serializer(serializers.ModelSerializer):

    class Meta:
        model = models.Report
        fields = ('id','title','description','reporter')


class Investment_Serializer(serializers.ModelSerializer):

    class Meta:
        model = models.Investment
        fields = ('id','project','investor','money_invested')
