from django.conf import settings
from django.db import models  
from django.utils import timezone

# Create your models here.
class Post(models.Model):  # models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # This is a link to another model
	title = models.CharField(max_length=200)  # Defining a text with a limited number of characters
	text = models.TextField()  # Long Text without a limit. For post contents.
	created_date = models.DateTimeField(default=timezone.now)  # This a date and time
	published_date = models.DateTimeField(blank=True, null=True)  

	def publish(self):
		self.published_date = timezone.now()  #  It saves the time of publishing
		self.save()  

	def __str__(self):  # Using "dunder" or "double-underscore"
		return self.title

