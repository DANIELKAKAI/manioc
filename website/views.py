from django.shortcuts import render
import requests
# Create your views here.

def home(request):
	res = requests.get('https://api.ona.io/api/v1/data/401455',auth=('danielkimassai','mylenana'))
	farmers = res.json()
	return render(request,"home.html",{'farmers':farmers})


def fields(request):
	res = requests.get('https://api.ona.io/api/v1/data/401002',auth=('danielkimassai','mylenana'))
	fields = res.json()
	return render(request,"fields.html",{'fields':fields})