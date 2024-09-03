from django.http import JsonResponse
from .models import SensorData  # Import the SensorData model

def receive_data(request, temperature, humidity, aqi, timestamp):
    if request.method == 'GET':
        try:
            # Convert parameters to the appropriate types
            temperature = float(temperature)
            humidity = float(humidity)
            aqi = str(aqi)
            timestamp = str(timestamp)

            # Log the received data (for debugging purposes)
            print(f"Received data: Temp={temperature}, Humidity={humidity}, AQI={aqi}, Timestamp={timestamp}")

            # Save the data to the database
            SensorData.objects.create(temperature=temperature, humidity=humidity, aqi=aqi)

            # Return a success response
            return JsonResponse({'status': 'success', 'message': 'Data received successfully'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    else:
        return JsonResponse({'status': 'error', 'message': 'Only GET requests are allowed'}, status=405)
