from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User_Profile)
admin.site.register(models.Project)
admin.site.register(models.Report)
admin.site.register(models.Investment)
