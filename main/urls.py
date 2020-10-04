from django.urls import path,include
from rest_framework import routers
from .views import EmployeeViewSet
router=routers.DefaultRouter()
router.register(r'employee',EmployeeViewSet)
urlpatterns=[
    path('',include(router.urls))
]