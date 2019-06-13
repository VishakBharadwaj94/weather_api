import requests 

def weather_info(city,units):
	url_base = 'http://api.openweathermap.org/data/2.5/weather?'
	appid = '3009ca0332d7a9e8726110d3756acfb3'
	if units == 'kelvin':

		url = url_base + f'q={city}' + f'&appid={appid}'
	else:
		url = url_base + f'q={city}' + f'&appid={appid}'+ f'&units={units}'
	
	return requests.get(url).json()

