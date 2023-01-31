from django.urls import path
from .views import RobotCreate

urlpatterns = [
    path('', RobotCreate.as_view(), name='robot-create')
]