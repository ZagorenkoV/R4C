from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Robot
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