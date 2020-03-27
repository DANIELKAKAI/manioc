from django.core.management.base import BaseCommand, CommandError
import requests
from website.models import Farmer

class Command(BaseCommand):
	help = 'put farmers data from ona to database'
	
	def handle(self,*args,**options):
		try:
			res = requests.get('https://api.ona.io/api/v1/data/401455',auth=('danielkimassai','mylenana'))
			farmers = res.json()
			Farmer.objects.create(data=farmers)
		except:
			raise CommandError('Error updating data')