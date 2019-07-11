from django.shortcuts import render
from polls.models import users
from polls.models import nearbyspots
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from polls.forms import EntryForm
from django.contrib.auth import authenticate, login

def index(request):
	return HttpResponse("Hello Riddhi Here")

@csrf_exempt
def login(request):
	#uname = request.POST['username']
	#password = request.POST['password']
	email = request.POST.get('email')
	password = request.POST.get('password')
	try:
		#user = authenticate(request, dusername=uname,dpassword=password)
		one = users.objects.get(email = email)
		two = users.objects.get(password = password)
		user = users.objects.filter(email=one).filter(password=two)
		return HttpResponse("OK")
	except users.DoesNotExist:
		return HttpResponse('NOTOK')
@csrf_exempt
def register(request):
	form = EntryForm(request.POST or None)
	if request.method ==  'POST' and form.is_valid():
		form.save()
	return HttpResponse('RRRegistered')

@csrf_exempt
def nearby(request):
	latitude =  request.POST.get('latitude')
	longitude = request.POST.get('longitude')
	print latitude
	print longitude
	#latitude = float( 22.3188)
	#longitude = float(73.1709)
	try:
		#one = '''select latitude,longitude (6371* acos(cos(radians(%s))*cos(radians(latitude))*cos(radians(longitude)-radians(%s))+sin(r	adians(%s))*sin(radians(latitude))) AS distance FROM spots having distance <20''',[latitude,longitude,latitude]
		#two = spots.objects.raw('select longitude  (6371* acos(cos(radians(%s))*cos(radians(latitude))*cos(radians(longitude)-radians(%s)+sin(radians(%s))*sin(radians(latitude)))) AS distance FROM spots having distance < 20',[ '%'+latitude+'%','%'+longitude+'%','%'+latitude+'%'])
		#json_stuff = simplejson.dumps({"OK" :one})
		#json_stuff = simplejson("OK")
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM (SELECT  sname,latitude, longitude,type_of_parking,charges, (6371 * acos(cos(radians(%s)) * cos(radians(latitude)) * cos(radians(longitude) - radians(%s)) + sin(radians(%s)) * sin(radians(latitude))))AS distance FROM polls_nearbyspots) AS distances WHERE distance <5",[latitude,longitude,latitude])
		#cursor.execute("SELECT * FROM (SELECT  latitude, longitude, (6371 * acos(cos(radians(22.3186083)) * cos(radians(latitude)) * cos(radians(longitude) - radians(73.1685833)) + sin(radians(22.3186083)) * sin(radians(latitude))))AS distance FROM polls_nearbyspots) AS distances WHERE distance <20")
		#data = cursor.fetchall()
		#json_stuff=serializers.serialize("json", data)
		#data =[str(row[0]) for row in cursor.fetchall()]
		#data1 = [str(row[1]) for row in cursor.fetchall()]
		
		
		#data = []
		#data1 = []
		#for row in cursor.fetchall():
			#data = str(row[0])
			#data1 = str(row[1])
		




		#rlen = len (cursor.fetchall())
		#i=0
		#while i < rlen :
		#	data = row[0] , row[1]
		#return HttpResponse(json_stuff, content_type="application/json")
		#return HttpResponse(data,content_type="application/json")
		


		
		#data_details = {'latitude': data , 'longitude':data1}
		#r_data = []
		#r_data.append(data_details)
		#r_data = json.dumps({'result':r_data})
		r = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
		ridd = json.dumps({'result':r}, cls = DjangoJSONEncoder)
		return HttpResponse(ridd,content_type='application/json')
		

		#ids = [row[0] for row in cursor.fetchall()]

		#return ids	
	except nearbyspots.DoesNotExist:
		return HttpResponse('NOT OK')

