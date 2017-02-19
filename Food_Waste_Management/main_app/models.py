from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
	rollNum = models.CharField(max_length = 8, unique = True)
	name = models.CharField(max_length = 100)
	branch = models.CharField(max_length = 10)
	hostel = models.CharField(max_length = 100)
	roomNum = models.CharField(max_length = 10)
	contactNum = models.CharField(max_length = 15)

	def __str__(self):
		return self.rollNum
