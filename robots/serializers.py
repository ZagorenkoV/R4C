from rest_framework import serializers
from .models import Robot

#сериалайзер, принимающий инфо для записи в БД
class RobotSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=2)
    version = serializers.CharField(max_length=2)
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',
        input_formats=['%Y-%m-%d %H:%M:%S'])

    def create(self, validated_data):
        return Robot.objects.create(**validated_data)