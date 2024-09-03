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

            # Log the received data (for debugging purposes)
            print(f"Received data: Device={device_id}, Temp={temperature}, Humidity={humidity}, AQI={aqi}, PPM={ppm}, Lat={latitude}, Long={longitude}")

            # Save the data to the database (timestamp will be set automatically)
            SensorData.objects.create(
                device_id=device_id,
                temperature=temperature,
                humidity=humidity,
                aqi=aqi,
                ppm=ppm,
                latitude=latitude,
                longitude=longitude
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

    # Fetch the latest sensor data for each device
    latest_data = {}
    for device in devices:
        device_id = device['device_id']
        latest_entry = SensorData.objects.filter(device_id=device_id).order_by('-timestamp').first()
        if latest_entry:
            latest_data[device_id] = latest_entry

    # Pass the devices and their latest data to the template
    return render(request, 'arduino/device_list.html', {'latest_data': latest_data})






def device_detail(request, device_id):
    # Fetch all sensor data for the specified device
    data = SensorData.objects.filter(device_id=device_id)

    # Pass the data to the template
    return render(request, 'arduino/device_detail.html', {'data': data, 'device_id': device_id})


import folium
from django.shortcuts import render
from .models import SensorData
from django.db.models import Max

def device_map(request):
    # Create a Folium map centered on a default location
    m = folium.Map(location=[23.8859, 45.0792], zoom_start=6)  # Centered on Saudi Arabia

    # Fetch the latest sensor data for each device using Max aggregation on the timestamp
    latest_device_data = SensorData.objects.values('device_id').annotate(latest_timestamp=Max('timestamp'))

    # Use a list comprehension to get the latest SensorData entries based on the latest timestamp for each device
    devices = [SensorData.objects.filter(device_id=data['device_id'], timestamp=data['latest_timestamp']).first() for data in latest_device_data]

    # Define AQI color mapping
    aqi_color_map = {
        "Green (Healthy)": "green",
        "Yellow (Moderate)": "yellow",
        "Orange (Unhealthy for Sensitive Groups)": "orange",
        "Red (Unhealthy)": "red",
        "Purple (Very Unhealthy)": "purple",
        "Brown (Hazardous)": "darkred"
    }

    # Add CircleMarker for each device on the map
    for device in devices:
        # Ensure the AQI category is correctly fetched and matched
        marker_color = aqi_color_map.get(device.aqi.strip(), "blue")  # Use strip() to remove any extra spaces

        # Debugging print to check the AQI value and color
        print(f"Device ID: {device.device_id}, AQI: {device.aqi}, Color: {marker_color}")

        folium.CircleMarker(
            location=[device.latitude, device.longitude],
            radius=8,  # Size of the circle marker
            popup=f'Device ID: {device.device_id}<br>Temperature: {device.temperature} °C<br>Humidity: {device.humidity} %<br>AQI: {device.aqi}',
            color=marker_color,  # Circle border color
            fill=True,
            fill_color=marker_color,  # Fill color matches the border color
            fill_opacity=0.7  # Slight transparency for better visualization
        ).add_to(m)

    # Generate HTML representation of the map
    map_html = m._repr_html_()

    # Pass the map to the template
    return render(request, 'arduino/device_map.html', {'map': map_html})

