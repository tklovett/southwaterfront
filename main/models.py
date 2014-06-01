from django.db import models

# Create your models here.
class GroceryStore(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	logo_url = models.URLField()

	def __str__(self):
		return "<GroceryStore: {0}>".format(self.name)


class Resident(models.Model):
	SPENDING_CHOICES = (
		("0", "$0-50"),
		("1", "$50-100"),
		("2", "$100-150"),
		("3", "$150-200"),
		("4", "$200+"),
	)
	given_name = models.CharField(max_length=35)
	family_name = models.CharField(max_length=35)
	email = models.EmailField(unique=True)
	monthly_spending = models.CharField(max_length=1, choices=SPENDING_CHOICES, blank=False, default="Choose one...")

	def __str__(self):
		return "<Resident: {0}>".format(self.email)


class Vote(models.Model):
	resident = models.ForeignKey('Resident')
	store = models.ForeignKey('GroceryStore')

	def __str__(self):
		return "<Vote: {0} {1}>".format(self.resident, self.store)