from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import json
from .models import SensorData  # Ensure your model is correctly imported


@csrf_exempt  # Disable CSRF verification for this view
def receive_data(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)

            # Extract data from the JSON payload
            device_id = data.get('device_id', 0)
            temperature = data.get('temperature')
            humidity = data.get('humidity')
            aqi = data.get('aqi')
            ppm = data.get('ppm')
            latitude = data.get('latitude', 18.2465)  # Default value if not provided
            longitude = data.get('longitude', 42.5117)  # Default value if not provided
            timestamp = data.get('timestamp')

            # Log the received data (for debugging purposes)
            print(f"Received data: Device={device_id}, Temp={temperature}, Humidity={humidity}, AQI={aqi}, PPM={ppm}, Lat={latitude}, Long={longitude}, Timestamp={timestamp}")

            # Save the data to the database
            SensorData.objects.create(
                device_id=device_id,
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
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)







def device_list(request):
    # Fetch all unique device IDs from the SensorData model
    devices = SensorData.objects.values('device_id').distinct()

    # Pass the devices to the template
    return render(request, 'device_list.html', {'devices': devices})





def device_detail(request, device_id):
    # Fetch all sensor data for the specified device
    data = SensorData.objects.filter(device_id=device_id)

    # Pass the data to the template
    return render(request, 'device_detail.html', {'data': data, 'device_id': device_id})
