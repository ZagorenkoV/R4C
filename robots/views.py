from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Robot
from .serializers import RobotSerializer

class RobotCreate(APIView):

    def get(self, request):
        queryset = Robot.objects.all()
        serializer_for_queryset = RobotSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)
    
    def post(self, request, format=None):
        serializer = RobotSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
