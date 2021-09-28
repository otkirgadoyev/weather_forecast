import requests
from django.shortcuts import render


def home(request):
    city=request.GET.get('city', 'Tashkent')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2cd473cb17321b0c0bd791b210e5e5de'
    data = requests.get(url).json()
    payload = {
        'city': data['name'],
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],
        'kelvin_temperature': data['main']['temp'],
        'celcius_temperature': int(data['main']['temp'])-273,
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }
    context={'data':payload}
    print(context)
    return render(request, 'home.html',context)
