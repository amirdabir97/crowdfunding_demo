from . import views
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user_profiles',views.User_Profile_Viewset)
router.register('projects',views.Project_Viewset)
router.register('login',views.Login_Viewset,basename = 'login')
router.register('reports',views.Report_Viewset)
router.register('investments',views.Investment_Viewset)


urlpatterns = [
    path('',include(router.urls))
]
