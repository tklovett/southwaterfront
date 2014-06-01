from django.db import models

# Create your models here.
class GroceryStore(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	logo_url = models.URLField()

	def __str__(self):
		return "<GroceryStore: {0}>".format(name)