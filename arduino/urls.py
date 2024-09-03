from django.urls import path
from .views import receive_data, device_list, device_detail, device_map

urlpatterns = [
    path('', device_map, name='device_map'),
    path('devices/', device_list, name='device_list'),
    path('devices/<int:device_id>/', device_detail, name='device_detail'),
    path('api/data/', receive_data, name='receive_data'),  # Ensure this matches exactly
]
