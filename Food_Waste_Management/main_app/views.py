from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from models import Student
import requests
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
	return render(request, 'index.html');

def load(request):
	#url = 'https://insite.iitmandi.ac.in/directory/students/iphd.php'

	r = requests.get(url)

	soup = BeautifulSoup(r.content,"lxml")

	data = soup.find_all('td');
	length = len(data)
	for i in range(3,length,9):
		rollNum = data[i].text
		name = data[i+1].text
		branch = data[i+2].text
		hostel = data[i+3].text
		roomNum = data[i+4].text
		contactNum = data[i+8].text
		student = Student(rollNum = rollNum,name = name,branch = branch,hostel = hostel,roomNum = roomNum,contactNum = contactNum) 
		student.save();
	return HttpResponse("Student loaded successfully")
