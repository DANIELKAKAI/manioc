from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.


class Farmer(models.Model):
	data = JSONField()


class Field(models.Model):
	data = JSONField()
