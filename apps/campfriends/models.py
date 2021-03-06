from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

from ..login.models import User

class LocationManager(models.Manager):
	def basic_validator(self, postData):
		response = {
			'status': False,
			'errors': []
		}
		if len(postData['loc_name']) < 1:
			response["errors"].append("Name of location should be at least 1 character")
		if len(postData['desc']) < 1:
			response["errors"].append("Please fill out the description")
		if len(response['errors']) == 0:
			response['status'] = True
			# create info here
			# loc_name= postData['loc_name'],
			# loc_latitude= postData['loc_latitude'],
			# loc_longitude= postData['loc_longitude']
			# desc= postData['desc']

				
			print(response)
		return response


class Location(models.Model):
	loc_name= models.CharField(max_length=255)
	loc_latitude= models.CharField(max_length=255)
	loc_longitude= models.CharField(max_length=255)
	desc= models.TextField(max_length=1000)
	creator= models.ForeignKey(User, related_name= 'created_camps')
	created_at= models.DateTimeField(auto_now_add = True)
	updated_at= models.DateTimeField(auto_now = True)
	objects = LocationManager()
	def __repr__(self):
		return "<Location object: {} {} {}>".format(self.loc_name, self.loc_address, self.desc)