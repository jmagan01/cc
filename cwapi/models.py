from django.db import models

# Create your models here.
class Product(models.Model):
	CATEGORIES = (
		('LAP', 'Laptop'),
		('CON', 'Console'),
		('GAD', 'Gadget'),
		('GAM', 'Game'),
		('TEL', 'TV')
	)
	title = models.CharField(max_length=255)
	description = models.CharField(max_length = 500)
	quantity = models.IntegerField()
	category = models.CharField(
	max_length=3,
	choices=CATEGORIES
	)
	date_posted = models.DateTimeField(auto_now_add=True, blank=True)
	def __str__(self):
		return self.title

