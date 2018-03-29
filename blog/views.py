from django.shortcuts import render
from .models import Post, Bird, Church
from django.views.generic import ListView
from django.utils import timezone
from django.views.static import serve
import os
import requests
import json

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_data(request):
	birds = Bird.objects.order_by('-date')[:10]
	# create or open the text file to hold the data.
	f= open("birddata.json", "w+")
	print("[")
	f.write("[")
	for bird in birds:
		print('{" Number": "%s"' % bird.id +
			',"Description": "%s"' % bird.description +
			',"Date": "%s"' % bird.date +
			',"Lat": "%s"' % bird.lat +
			',"Long": "%s"},' % bird.lon)
		f.write('{" Number": "%s"' % bird.id +
			',"Description": "%s"' % bird.description +
			',"Date": "%s"' % bird.date +
			',"Lat": "%s"' % bird.lat +
			',"Long": "%s"},' % bird.lon)
	print("]")
	f.write("]")
	f.close()
	# return render(request, 'blog/post_data.html', {'birds': birds})
	# Linux vs. Windows
	filepath = "/home/jmeroth/birddata.json"
	#filepath = r"C:\Users\jmeroth\djangogirls\birddata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def church_data(request):
	churches = Church.objects.order_by('-date')[:10]
	# create or open the text file to hold the data.
	f= open("churchdata.json", "w+")
	print("[")
	f.write("[")
	for church in churches:
		print('{" Number": "%s"' % church.id +
			',"Description": "%s"' % church.description +
			',"Date": "%s"' % church.date +
			',"Lat": "%s"' % church.lat +
			',"Long": "%s"},' % church.lon)
		f.write('{" Number": "%s"' % church.id +
			',"Description": "%s"' % church.description +
			',"Date": "%s"' % church.date +
			',"Lat": "%s"' % church.lat +
			',"Long": "%s"},' % church.lon)
	print("]")
	f.write("]")
	f.close()
	# return render(request, 'blog/church_data.html', {'churches': churches})
	# Linux vs. Windows
	filepath = "/home/jmeroth/churchdata.json"
	#filepath = "C:\\Users\\jmeroth\\djangogirls\\churchdata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def crime_data(request):
	# create or open the text file to hold the data.
	f= open("crimedata.json", "w+")
	f.write("[")
	# Retrieve data from data.boston.gov where "limit" is num of records returned.
	url = "https://data.boston.gov/api/3/action/datastore_search?resource_id=12cb3883-56f5-47de-afa5-3b1cf61b257b&limit=20000"
	r = requests.get(url)
	myCount = 0
	if(str(r) == "<Response [200]>"):
		myjson = r.json()
	else:
		print (r)
		print("'GET' response error")
	# Once "myjson" is defined:
	for i in myjson['result']['records']:
		if (i['SHOOTING'] == 'Y'):
			f.write('{" Number": "%s"' % str(i["_id"]) +
			',"Description": "%s"' % str(i["OFFENSE_CODE_GROUP"]) +
			',"Date": "%s"' % str(i['OCCURRED_ON_DATE']) +
			',"Lat": "%s"' % str(i['Lat']) +
			',"Long": "%s"},' % str(i['Long']))
	f.write("]")
	f.close()
	# Linux vs. Windows
	filepath = "/home/jmeroth/crimedata.json"
	#filepath = "C:\\Users\\jmeroth\\djangogirls\\crimedata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))