from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt  # Disable CSRF verification for this view
def receive_data(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)

            # Extract temperature, humidity, and AQI values from the JSON data
            temperature = data.get('temperature')
            humidity = data.get('humidity')
            aqi = data.get('aqi')

            # Log the received data (for debugging purposes)
            print(f"Received data: Temp={temperature}, Humidity={humidity}, AQI={aqi}")

            # Here you can process the data or save it to the database
            # For example:
            # SensorData.objects.create(temperature=temperature, humidity=humidity, aqi=aqi)

            # Return a success response
            return JsonResponse({'status': 'success', 'message': 'Data received successfully'})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)
