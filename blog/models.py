from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Bird(models.Model):
	description = models.CharField(max_length=200)
	latin = models.CharField(max_length=200, null=True, blank=True)
	date = models.DateTimeField(default=timezone.now)
	address = models.CharField(max_length=200, null=True, blank=True)
	lat = models.CharField(max_length=20, null=True, blank=True)
	lon = models.CharField(max_length=20, null=True, blank=True)
	bird_pic = models.ImageField(upload_to = 'images/%Y/%m/%d/', null=True, blank=True)

	def __str__(self):
		return self.description


class Church(models.Model):
	description = models.CharField(max_length=200)
	date = models.DateTimeField(default=timezone.now)
	lat = models.CharField(max_length=20)
	lon = models.CharField(max_length=20)

	def __str__(self):
		return self.description



class Violation(models.Model):
	pwsid = models.CharField(max_length=200)
	violation_id = models.CharField(max_length=200)
	compl_per_begin_date = models.CharField(max_length=200, blank=True, null=True)
	# is_health_based_ind = models.BooleanField(default=False)
	is_health_based_ind = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return self.pwsid
		


class WaterSystem(models.Model):
	# boolean_field = models.BooleanField(default=False)
	city_name = models.CharField(max_length=200, null=True, blank=True)
	gw_sw_code = models.CharField(max_length=200, null=True, blank=True)
	population_served_count = models.IntegerField(default=0)
	pwsid = models.CharField(max_length=200, null=True, blank=True)
	pws_activity_code = models.CharField(max_length=200, null=True, blank=True)
	pws_name = models.CharField(max_length=200, null=True, blank=True)
	state_code = models.CharField(max_length=20, null=True, blank=True)
	zip_code = models.CharField(max_length=10, null=True, blank=True)
	counties_served = models.CharField(max_length = 200, null=True, blank=True)
	cities_served = models.CharField(max_length = 200, null=True, blank=True)
	pws_type_code = models.CharField(max_length=6, blank=True, null=True)
	primacy_agency_code = models.CharField(max_length=2, null=True, blank=True)

	def __str__(self):
		return self.pwsid


