from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
	CONDITION_TYPE = (
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
	item_id = models.AutoField(
		primary_key=True, 
		unique=True,
		verbose_name='Item identifier',)
	item_title = models.CharField(
		max_length = 100,
		verbose_name='Item Title',)
	quantity = models.IntegerField(
		verbose_name='Quantity',)
	condition =  models.CharField(
		max_length = 1,
		choices=CONDITION_TYPE,
		verbose_name='Condition of the Item'
	)
	description = models.CharField(
		max_length = 255,
		verbose_name='Item Description')
	category = models.CharField(
		max_length = 3,
		choices=CATEGORIES,
		verbose_name='Item Category'
	)
	date_posted = models.DateTimeField(
		auto_now_add=True, 
		blank=True)
	expiry_date = models.DateTimeField()
	seller = models.CharField(max_length = 25)
	# seller = models.ForeignKey(
        # settings.AUTH_USER_MODEL,
        # on_delete=models.CASCADE,
    # )
	def __str__(self):
		return self.item_title
	
	# The get_absolute_url() method sets a canonical URL for the model. 
	# This is required when using the reverse() function. 
	# It is the correct way to refer to a model in templates to avoid hard-coding.
	def get_absolute_url(self):
		return reverse('item_list', args=[str(self.id)])
		
class Auction(Item):
	auction_id = models.AutoField(
		primary_key=True, 
		unique=True,
		verbose_name='Auction identifier')
	time_left = models.DurationField(
		verbose_name='Time left to complete'
		)
	
	def __str__(self):
		return self.item_title
	
	def get_absolute_url(self):
		return reverse('auction_list', args=[str(self.id)])