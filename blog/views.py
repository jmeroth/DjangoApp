from django.shortcuts import render
from .models import Post, Bird, Church
from django.views.generic import ListView
from django.utils import timezone
from django.views.static import serve
import os
import requests
import json
import folium
from folium import IFrame


# Utility functions

def mymap(request):

	map = folium.Map(location=[42.34, -71.1], zoom_start=12, tiles="cartodbdark_matter")
	# Stamen Terrain
	# Mapbox Bright
	# Mapbox Control Room - dark with cities in green.
	# stamenwatercolor - very colorfull
	# cartodbpositron - grey, best
	birds = Bird.objects.order_by('-date')[:15]
	# Creates arrays from the database objects to zip and provide the data for markers.
	lat = []
	lon = []
	des = []
	lin = []
	for bird in birds:
		lat.append(float(bird.lat))
		lon.append(float(bird.lon))
		des.append(bird.description)
		lin.append(str("" if bird.latin is None else bird.latin))
		print(bird.lat, bird.lon, bird.description, bird.latin)
	fgb = folium.FeatureGroup(name="Birds")
	for lt, ln, ds, li in zip(lat, lon, des, lin):
		text = ds + "<br>" + li
		# Using folium IFrame to format popup using HTML element.
		p = folium.Popup(IFrame(text, width=180, height=80))
		fgb.add_child(folium.CircleMarker(location=[lt, ln]
											, popup=p
											, color='green'
											, radius=4
											, fill_color='green'
											, fill=True
											, fill_opacity=0.7))
	map.add_child(fgb)
	map.add_child(folium.LayerControl())

	# for dev/ Windows:
	#map.save("blog/templates/Map1.html")
	#return render(request, 'Map1.html',)

	# for prod/ Linux
	#map.save("Map1.html")
	#filepath = "/home/jmeroth/Map1.html"
	#return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

	if os.name == 'nt':
		map.save("blog/templates/Map1.html")
		return render(request, 'Map1.html',)
	else:
		map.save("Map1.html")
		filepath = "/home/jmeroth/Map1.html"
		return serve(request, os.path.basename(filepath), os.path.dirname(filepath))




def addr_to_coords(add_string):
	# stub - function will call geocode api
	MY_API_KEY = "AIzaSyB6MPTDLVXsah1pC28PswyBvl7Ze6-83vM"
	baseUrl = "https://maps.googleapis.com/maps/api/geocode/json"
	myUrl =  baseUrl + "?address=" + add_string + "&key=" + MY_API_KEY
	r = requests.get(myUrl)
	print(r)
	if(str(r) == "<Response [200]>"):
		myjson = r.json()
	else:
		print(r)
		print("'GET' response error")
	# Returns a dictionary of 'lat' and 'lng' values.
	return myjson["results"][0]["geometry"]["location"]


# menu view

def menu(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'base.html', {'posts': posts})

# list view

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# bird_api view

def bird_api(request):
    birds = Bird.objects.all()  #  filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/bird_api.html', {'birds': birds})

# data views

def post_data(request):
	birds = Bird.objects.order_by('-date')[:15]
	# create or open the text file to hold the data.
	with open("birddata.json", "w+") as f:
		print("[")
		f.write("[")
		for bird in birds:
			print('{" Number": "%s"' % bird.id +
				',"Description": "%s"' % bird.description +
				',"Latin": "%s"' % ("" if bird.latin is None else bird.latin) +
				',"Date": "%s"' % bird.date +
				',"Lat": "%s"' % bird.lat +
				',"Long": "%s"},' % bird.lon)
			f.write('{" Number": "%s"' % bird.id +
				',"Description": "%s"' % bird.description +
				',"Latin": "%s"' % ("" if bird.latin is None else bird.latin) +
				',"Date": "%s"' % bird.date +
				',"Lat": "%s"' % bird.lat +
				',"Long": "%s"},' % bird.lon)
		print("]")
		f.write("]")
	# return render(request, 'blog/post_data.html', {'birds': birds})
	# Linux vs. Windows
	if os.name == 'nt':
		filepath = r"C:\Users\jmeroth\djangogirls\birddata.json"
	else:
		filepath = "/home/jmeroth/birddata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def church_data(request):
	churches = Church.objects.order_by('-date')[:10]
	# create or open the text file to hold the data.
	with open("churchdata.json", "w+") as f:
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
	# return render(request, 'blog/church_data.html', {'churches': churches})
	# Linux vs. Windows
	if os.name == 'nt':
		filepath = "C:\\Users\\jmeroth\\djangogirls\\churchdata.json"
	else:
		filepath = "/home/jmeroth/churchdata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def crime_data(request):
	# create or open the text file to hold the data.
	with open("crimedata.json", "w+") as f:
		f.write("[")
		# Retrieve data from data.boston.gov where "limit" is num of records returned.
		url = "https://data.boston.gov/api/3/action/datastore_search?resource_id=12cb3883-56f5-47de-afa5-3b1cf61b257b&limit=10000"
		r = requests.get(url)
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
	# Linux vs. Windows
	if os.name == 'nt':
		filepath = "C:\\Users\\jmeroth\\djangogirls\\crimedata.json"
	else:
		filepath = "/home/jmeroth/crimedata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def construction_data(request):
	# create or open the text file to hold the data.
	with open("constructiondata.json", "w+") as f:
		f.write("[")
		# Retrieve data from data.boston.gov where "limit" is num of records returned.
		url = "https://data.boston.gov/api/3/action/datastore_search?resource_id=36fcf981-e414-4891-93ea-f5905cec46fc&limit=10"
		r = requests.get(url)
		if(str(r) == "<Response [200]>"):
			myjson = r.json()
		else:
			print (r)
			print("'GET' response error")
		# Once "myjson" is defined:
		#print(myjson)
		for i in myjson['result']['records']:
			address_string = i['Address1']+' '+i['Street']+' '+i['Neighborhood']+' MA'
			#if (i['ProjectCategory'] == 'EMERGENCY'):
			if (True):
				f.write('{" Number": "%s"' % str(i["Permit"]) +
				',"Description": "%s"' % str(i["ConstructionNotes"]) +
				',"Date": "%s"' % str(i['ExpirationDate']) +
				',"Lat": "%s"' % str(addr_to_coords(address_string)["lat"]) +
				',"Long": "%s"},' % str(addr_to_coords(address_string)["lng"]))
		f.write("]")
	# Linux vs. Windows
	if os.name == 'nt':
		filepath = "C:\\Users\\jmeroth\\djangogirls\\constructiondata.json"
	else:
		filepath = "/home/jmeroth/constructiondata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def permit_data(request):
	# create or open the text file to hold the data.
	with open("permitdata.json", "w+") as f:
		f.write("[")
		# Retrieve data from data.boston.gov.  Limit = number of records.
		url = "https://data.boston.gov/api/3/action/datastore_search?resource_id=6ddcd912-32a0-43df-9908-63574f8c7e77&q=2018-&limit=10"
		r = requests.get(url)
		if(str(r) == "<Response [200]>"):
			myjson = r.json()
		else:
			print (r)
			print("'GET' response error")
		# Once "myjson" is defined:
		for i in myjson['result']['records']:
			address_string = i['ADDRESS']+' '+i['CITY']+' '+i['STATE']+' '+i['ZIP']
			if (i['STATUS'] == 'Open'):
				f.write('{" Number": "%s"' % str(i["PermitNumber"]) +
				',"Description": "%s"' % str(i["Comments"]) +
				',"Date": "%s"' % str(i['ISSUED_DATE']) +
				#',"Lat": "%s"' % str(addr_to_coords(address_string)[0]) +
				',"Lat": "%s"' % str(i['Location'][1:9]) +
				#',"Long": "%s"},' % str(addr_to_coords(address_string)[1]))
				',"Long": "%s"},' % str(i['Location'][15:24]))
		f.write("]")
	# Linux vs. Windows
	if os.name == 'nt':
		filepath = "C:\\Users\\jmeroth\\djangogirls\\permitdata.json"
	else:
		filepath = "/home/jmeroth/permitdata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


def tree_data(request):
	# create or open the text file to hold the data.
	with open("treedata.json", "w+") as f:
		f.write("[")
		# Retrieve data from data.boston.gov.
		url = "https://data.boston.gov/api/3/action/datastore_search?resource_id=2968e2c0-d479-49ba-a884-4ef523ada3c0&q=tree"
		r = requests.get(url)
		if(str(r) == "<Response [200]>"):
			myjson = r.json()
		else:
			print (r)
			print("'GET' response error")
		# Once "myjson" is defined:
		for i in myjson['result']['records']:
			if i['QUEUE'] == 'PARK_Tree Maintenance Request':				
				f.write('{" Number": "%s"' % str(i["CASE_ENQUIRY_ID"]) +
				',"Description": "%s"' % str(i["CLOSURE_REASON"]) +
				',"Date": "%s"' % str(i['open_dt']) +
				',"Lat": "%s"' % str(i['Latitude']) +
				',"Long": "%s"' % str(i['Longitude']) +
				',"submittedphoto": "%s"},' % str(i["SubmittedPhoto"]))
		f.write("]")
	# Linux vs. Windows
	if os.name == 'nt':
		filepath = "C:\\Users\\jmeroth\\djangogirls\\treedata.json"
	else:
		filepath = "/home/jmeroth/treedata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))