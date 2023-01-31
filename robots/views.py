import pandas as pd

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from datetime import timedelta, timezone

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
    
class RobotReport(View):
    def get(self, request):
        # собираем всех роботов произведенных за неделю
        robots = Robot.objects.filter(created_gte=timezone.now() - timedelta(days=7))
        
        # делаем подсчет сколько роботов было произведено каждой модели+версии
        report = robots.values('model', 'version').annotate(total=Count("id"))
        
        # создаем excel файл с страницами под каждую модель
        writer = pd.ExcelWriter('robot_report.xlsx', engine='xlsxwriter')
        for model, data in report.groupby('model'):
            data.to_excel(writer, sheet_name=model, columns = ['Model', 'Version', 'Avg Score'])
        writer.save()
        with open('robot_report.xlsx', 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'attachment; filename=robot_report.xlsx'
            return response
