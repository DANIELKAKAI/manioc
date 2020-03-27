from django.shortcuts import render
import requests
from website.models import Farmer,Field
# Create your views here.

def home(request):
	farmers = Farmer.objects.last().data
	return render(request,"home.html",{'farmers':farmers})


def fields(request):
	fields = Field.objects.last().data
	return render(request,"fields.html",{'fields':fields})

