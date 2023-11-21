# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer
from django.shortcuts import get_object_or_404


class CreateAPIView(APIView):
    allowed_methods = ['GET', 'POST', 'PATCH']

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            sensor = Sensor.objects.get(id=pk)
        except Sensor.DoesNotExist:
            return Response({"detail": "Объект не найден."}, status=status.HTTP_404_NOT_FOUND)
        description = request.data.get('description')
        if description is not None:
            sensor.description = description
            sensor.save()
            serializer = SensorSerializer(sensor)
            return Response(serializer.data)
        else:
            return Response({"description": ["Это поле является обязательным."]}, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateAPIView(APIView):
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCreateAPIView(APIView):
    def get(self, request, pk):
        sensor = get_object_or_404(Sensor, id=pk)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data, status=status.HTTP_200_OK)
