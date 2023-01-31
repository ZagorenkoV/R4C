from django.urls import path
from .views import RobotCreate
from .views import RobotReport

urlpatterns = [
    path('', RobotCreate.as_view(), name='robot-create'),
    path('report', RobotReport.as_view(), name='robot-report')
]