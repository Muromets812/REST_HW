from rest_framework import serializers
from datetime import datetime
from .models import Measurement, Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        sensor = Sensor.objects.create(**validated_data)
        return sensor

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance


class MeasurementSerializer(serializers.ModelSerializer):
    sensor = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all())

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

    def create(self, validated_data):
        validated_data['created_at'] = datetime.now()

        measurement = Measurement.objects.create(**validated_data)
        return measurement


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
