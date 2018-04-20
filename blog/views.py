from django.shortcuts import render
from .models import Post, Bird, Church
from django.views.generic import ListView
from django.utils import timezone
from django.views.static import serve
import os
import requests
import json

# Utility functions.

def addr_to_coords(add_string):
	# stub - function will call geocode api
	#MY_API_KEY = "AIzaSyB6MPTDLVXsah1pC28PswyBvl7Ze6-83vM"
	#https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
	#baseUrl = "https://maps.googleapis.com/maps/api/geocode/json"
	#myUrl =  baseUrl + "?address=" + add_string + "&key=" + MY_API_KEY
	#print(myUrl)
	print("Function addr_to_coords() = %s" % add_string)
	return (42.000, -71.000)

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
	url = "https://data.boston.gov/api/3/action/datastore_search?resource_id=12cb3883-56f5-47de-afa5-3b1cf61b257b&limit=10000"
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


def construction_data(request):
	# create or open the text file to hold the data.
	f= open("constructiondata.json", "w+")
	f.write("[")
	# Retrieve data from data.boston.gov where "limit" is num of records returned.
	url = "https://data.boston.gov/export/36f/cf9/36fcf981-e414-4891-93ea-f5905cec46fc.json"
	r = requests.get(url)
	myCount = 0
	if(str(r) == "<Response [200]>"):
		myjson = r.json()
	else:
		print (r)
		print("'GET' response error")
	# Once "myjson" is defined:
	for i in myjson:
		address_string = i['Address1']+' '+i['Street']+' '+i['Neighborhood']+' MA'
		if (i['ProjectCategory'] == 'EMERGENCY'):
			f.write('{" Number": "%s"' % str(i["Permit"]) +
			',"Description": "%s"' % str(i["ConstructionNotes"]) +
			',"Date": "%s"' % str(i['ExpirationDate']) +
			',"Lat": "%s"' % str(addr_to_coords(address_string)[0]) +
			',"Long": "%s"},' % str(addr_to_coords(address_string)[1]))
	f.write("]")
	f.close()
	# Linux vs. Windows
	filepath = "/home/jmeroth/constructiondata.json"
	#filepath = "C:\\Users\\jmeroth\\djangogirls\\constructiondata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


#  Approved building permits
def permit_data(request):
	# create or open the text file to hold the data.
	f= open("permitdata.json", "w+")
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
	f.close()
	# Linux vs. Windows
	filepath = "/home/jmeroth/permitdata.json"
	#filepath = "C:\\Users\\jmeroth\\djangogirls\\permitdata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


#  311 tree
def tree_data(request):
	# create or open the text file to hold the data.
	f= open("treedata.json", "w+")
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
		if (i['QUEUE'] == 'PARK_Tree Maintenance Request'):
			f.write('{" Number": "%s"' % str(i["CASE_ENQUIRY_ID"]) +
			',"Description": "%s"' % str(i["CLOSURE_REASON"]) +
			',"Date": "%s"' % str(i['open_dt']) +
			',"Lat": "%s"' % str(i['Latitude']) +
			',"Long": "%s"' % str(i['Longitude']) +
			',"submittedphoto": "%s"},' % str(i["SubmittedPhoto"]))
	f.write("]")
	f.close()
	# Linux vs. Windows
	filepath = "/home/jmeroth/treedata.json"
	#filepath = "C:\\Users\\jmeroth\\djangogirls\\treedata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))