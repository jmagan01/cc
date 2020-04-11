from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
	CONDITIONS = (
		('N', 'New'),
		('U', 'Used')
	)
	CATEGORIES = (
		('A&C', 'Antiques & Collectibles'),
		('AUT', 'Automotive'),
		('BOK', 'Books'),
		('C&A', 'Clothing & Accessories'),
		('E&C', 'Electronics & Computers'),
		('H&G', 'Home & Garden'),
		('JEW', 'Jewellery'),
		('L&T', 'Luggage & Travel'),
		('MUS', 'Musical Instruments'),
		('OFF', 'Office Products'),
		('S&V', 'Software & Videogames'),
		('T&E', 'Tools & Equipment'),
		('TOY', 'Toys')	
	)
	item_id = models.AutoField(primary_key=True, unique=True)
	item_title = models.CharField(max_length = 100)
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
	date_posted = models.DateTimeField(auto_now_add=True, blank=True)
	expiry_date = models.DateTimeField()
	# seller = models.ForeignKey(
        # settings.AUTH_USER_MODEL,
        # on_delete=models.CASCADE,
    # )
	seller = models.CharField(max_length = 25)
	def __str__(self):
		return self.item_title

