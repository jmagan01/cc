from django.conf import settings
from django.db import models

# Create your models here.
class Item(models.Model):
	CONDITIONS = (
		('N', 'New'),
		('U', 'Used')
	)
	CATEGORIES = (
		('LAP', 'Laptop'),
		('CON', 'Console'),
		('GAD', 'Gadget'),
		('GAM', 'Game'),
		('TEL', 'TV')
	)
	item_id = models.AutoField(primary_key=True, unique=True)
	item_title = models.CharField(max_length = 100)
	date_posted = models.DateTimeField(auto_now_add=True, blank=True)
	quantity = models.IntegerField()
	condition =  models.CharField(
		max_length = 1,
		choices=CONDITIONS
	)
	description = models.CharField(max_length = 255)
	category = models.CharField(
		max_length = 3,
		choices=CATEGORIES
	)
	expiry_date = models.DateTimeField()
	#seller = models.ForeignKey(
    #    settings.AUTH_USER_MODEL,
    #    on_delete=models.CASCADE,
    #)
	def __str__(self):
		return self.item_title

