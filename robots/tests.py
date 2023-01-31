import pandas as pd

from django.urls import reverse
from django.test import RequestFactory, TestCase
from django.utils import timezone

from datetime import timedelta

from rest_framework import status
from rest_framework.test import APITestCase
from .models import Robot
from .views import RobotReport
from .serializers import RobotSerializer

class RobotCreateTestCase(APITestCase):
    def setUp(self):
        self.data = {'model':'R2','version':'D2','created':'2022-12-31 23:59:59'}

    def test_get_robots(self):
        Robot.objects.create(**self.data)
        url = reverse("robot-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        robots = Robot.objects.all()
        serializer = RobotSerializer(instance=robots, many=True)
        self.assertEqual(response.data, serializer.data)
        
    def test_post_robot(self):
        url = reverse("robot-create")
        response = self.client.post(url, data=self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Robot.objects.count(), 1)
        robot = Robot.objects.get(id=response.data["id"])
        serializer = RobotSerializer(instance=robot)
        self.assertEqual(response.data, serializer.data)

    def test_create_robot_with_invalid_data(self):
        url = reverse("robot-create")
        invalid_data = {'model':'R-2','version':'D2','created':'2022-12-31 23:59:59'}
        response = self.client.post(url, data=invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Robot.objects.count(), 0)

class RobotReportTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    def test_robot_report(self):    
        request = self.factory.get('/robot-report/')
        robot1 = Robot.objects.create(
            model='R1', version='D2', created=timezone.now()
        )
        robot2 = Robot.objects.create(
            model='R1', version='D3', created=timezone.now() - timedelta(days=8)
        )
        response = RobotReport.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename=robot_report.xlsx')
        self.assertEqual(response['Content-Type'], 'application/vnd.ms-excel')
        
        df = pd.read_excel(response.content, sheet_name='R1')
        self.assertEqual(len(df), 1)
        self.assertEqual(df.loc[0]['Model'], 'R1')
        self.assertEqual(df.loc[0]['Version'], 'D2')
        self.assertEqual(df.loc[0]['Total'], None)