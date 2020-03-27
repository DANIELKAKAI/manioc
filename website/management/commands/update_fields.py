from django.core.management.base import BaseCommand, CommandError
import requests
from website.models import Field

class Command(BaseCommand):
	help = 'put fields data from ona to database'
	
	def handle(self,*args,**options):
		try:
			res = requests.get('https://api.ona.io/api/v1/data/401002',auth=('danielkimassai','mylenana'))
			fields = res.json()
			Field.objects.create(data=fields)
		except:
			raise CommandError('Error updating data')