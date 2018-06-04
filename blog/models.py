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

	def __str__(self):
		return self.description


class Church(models.Model):
	description = models.CharField(max_length=200)
	date = models.DateTimeField(default=timezone.now)
	lat = models.CharField(max_length=20)
	lon = models.CharField(max_length=20)

	def __str__(self):
		return self.description

