from django.shortcuts import render
from .models import Post, Bird, Church
from django.views.generic import ListView
from django.utils import timezone
from django.views.static import serve
import os

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
	# filepath = "/home/jmeroth/birddata.json"
	filepath = "C:\\Users\\jmeroth\\djangogirls\\birddata.json"
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
	# filepath = "/home/jmeroth/churchdata.json"
	filepath = "C:\\Users\\jmeroth\\djangogirls\\churchdata.json"
	return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

