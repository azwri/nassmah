from django.urls import path
from .views import receive_data

urlpatterns = [
    path('api/data/<str:temperature>/<str:humidity>/<str:aqi>/<str:timestamp>/', receive_data, name='receive_data'),
]
