from django.shortcuts import render
from urllib.request import urlopen
# import requests
import json
# Create your views here.

def home(request):
	# ip_address=request.META.get('HTTP_X_FORWARDED_FOR','')
	# print(ip_address)
	# return(render(request,'home.html',{'ip':ip_address}))
	response=urlopen('https://ipinfo.io/json')
	geodata=json.load(response)
	res=urlopen('https://api.openweathermap.org/data/2.5/weather?appid=f0769385c648750adf1041bbb6b6a8cb&q=%s,%s' %(geodata['city'],geodata['country']))
	data=json.load(res)
	print(data)
	temperature=data['main']['temp']
	return(
		render(request,'home.html',{
			'ip':geodata['ip'],
			'country':geodata['country'],
			'region':geodata['region'],
			'city':geodata['city'],
			'org':geodata['org'],
			'loc':geodata['loc'],
			'temp':temperature
		})
	)