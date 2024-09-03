from django.urls import path
from .views import receive_data  # Ensure your view is correctly imported

urlpatterns = [
    path('api/data/', receive_data, name='receive_data'),  # Ensure this matches exactly
]
