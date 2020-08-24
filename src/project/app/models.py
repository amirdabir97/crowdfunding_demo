from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User_Profile_Manager(BaseUserManager):

    def create_user(self , email , name , family_name , role , password = None):

        email = self.normalize_email(email)
        user = self.model(email = email , name = name , family_name = family_name , role = role)
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self , email , name , family_name , role , password):

        user = self.create_user(email = email ,name =  name ,family_name = family_name ,role = role,password = password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user


class User_Profile(PermissionsMixin , AbstractBaseUser):

    email = models.EmailField(unique = True , max_length = 255)
    name = models.CharField(max_length = 255)
    family_name = models.CharField(max_length = 255)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    role_choices = (('producer','producer'),('investor','investor'),('3rd_party','3rd_party'))

    role = models.CharField(max_length = 25 , choices = role_choices)

    objects = User_Profile_Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','family_name','role']

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return self.name + ' ' + self.family_name

    def __str__(self):
        return self.name + ' ' + self.family_name


class Project(models.Model):

    title = models.CharField(max_length = 255)
    topic = models.CharField(max_length = 255)
    description = models.CharField(max_length = 2550)
    estimated_time = models.IntegerField()
    needed_money = models.IntegerField()
    location = models.CharField(max_length = 255)
    producer = models.ForeignKey(User_Profile , on_delete = models.CASCADE , related_name = 'producing_projects')
    #investors = models.ManyToManyField(User_Profile,related_name = 'investing_projects',blank = True)


    def __str__(self):
        return self.title


class Report(models.Model):

    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 2550)
    reporter = models.ForeignKey(User_Profile,on_delete = models.CASCADE,related_name = 'reports')

    def __str__(self):
        return self.title


class Investment(models.Model):

    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='investments')
    investor = models.ForeignKey(User_Profile,on_delete=models.CASCADE,related_name='investments')
    money_invested = models.IntegerField()

    def __str__(self):
        return str(self.project)
