from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import SensorData  # Import the SensorData model

@csrf_exempt
def receive_data(request):
    if request.method == 'GET':
        try:
            # Extract data from query parameters
            temperature = request.GET.get('temperature')
            humidity = request.GET.get('humidity')
            aqi = request.GET.get('aqi')

            # Log the received data (for debugging purposes)
            print(f"Received data: Temp={temperature}, Humidity={humidity}, AQI={aqi}")

            # Save the data to the database
            SensorData.objects.create(temperature=temperature, humidity=humidity, aqi=aqi)

            # Return a success response
            return JsonResponse({'status': 'success', 'message': 'Data received successfully'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    else:
        return JsonResponse({'status': 'error', 'message': 'Only GET requests are allowed'}, status=405)
