from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import SensorData, Device  # Ensure your models are correctly imported
from django.contrib.auth.models import User  # Import User model to reference the user

@csrf_exempt  # Disable CSRF verification for this view
def receive_data(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)

            # Extract data from the JSON payload
            device_id = data.get('device_id')
            temperature = data.get('temperature')
            humidity = data.get('humidity')
            aqi = data.get('aqi')
            ppm = data.get('ppm')
            latitude = data.get('latitude', 18.2465)  # Default value if not provided
            longitude = data.get('longitude', 42.5117)  # Default value if not provided
            timestamp = data.get('timestamp')

            # Log the received data (for debugging purposes)
            print(f"Received data: Device={device_id}, Temp={temperature}, Humidity={humidity}, AQI={aqi}, PPM={ppm}, Lat={latitude}, Long={longitude}, Timestamp={timestamp}")

            # Fetch the default user (with ID 1)
            user = User.objects.get(id=1)
            
            # Fetch the device object
            device = Device.objects.get(device_id=device_id)

            # Save the data to the database
            SensorData.objects.create(
                user=user,  # Set the default user
                user_type='user',  # You can change this if needed
                device=device,
                temperature=temperature,
                humidity=humidity,
                aqi=aqi,
                ppm=ppm,
                latitude=latitude,
                longitude=longitude,
                timestamp=timestamp
            )

            # Return a success response
            return JsonResponse({'status': 'success', 'message': 'Data received successfully'})
        
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User does not exist'}, status=400)
        
        except Device.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Device does not exist'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)
