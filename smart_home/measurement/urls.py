from django.urls import path

from .views import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

urlpatterns = [
    path('sensors/', CreateAPIView.as_view(), name="create_sensor"),
    path('measurement/', RetrieveUpdateAPIView.as_view(), name="create_measurment"),
    path('sensors/<pk>/', CreateAPIView.as_view(),  name="update_sensor"),
    path('sensor/<pk>/', ListCreateAPIView.as_view(), name="create_list_sensor"),


]
