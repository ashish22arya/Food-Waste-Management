from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
	rollNum = models.CharField(max_length = 8, unique = True)
	name = models.CharField(max_length = 100)
	branch = models.CharField(max_length = 10)
	hostel = models.CharField(max_length = 100)
	roomNum = models.IntegerField()
	contactNum = models.CharField(max_length = 15)

	def __init__(self,rollNum, name, branch, hostel, roomNum, contactNum):
		self.rollNum = rollNum
		self.name = name
		self.branch = branch
		self.hostel = hostel
		self.roomNum = roomNum
		self.contactNum = contactNum
	def __str__(self):
		return self.rollNum
