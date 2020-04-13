from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import string
import random

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
	item_title = models.CharField(max_length=100,verbose_name='Item Title')
	starting_price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name='Starting Price')
	quantity = models.IntegerField(verbose_name='Quantity')
	condition = models.CharField(max_length = 1,choices=CONDITION_TYPE,verbose_name='Condition of the Item')
	description = models.TextField(
		verbose_name='Item Description')
	category = models.CharField(max_length = 3,choices=CATEGORIES,verbose_name='Item Category')
	date_posted = models.DateTimeField(auto_now_add=True, editable=False)
	expiry_date = models.DateTimeField()
	seller = models.CharField(max_length = 25) #? Get it from oAuth
	
	@property
	def time_left(self):
		td = abs(datetime.now() - self.expiry_date)
		totalmin, seconds = divmod(td.seconds, 60)
		hour, minutes = divmod(totalmin, 60)
		return '{} Days, {} Hours, {} Minutes, {} Seconds'.format(td.days, hour,minutes,seconds)
	
	#default = models.DateTimeField(expiry_date)#datetime.now()
	#
	# def save(self, *args, **kargs):
		# self.time_left = get_time_left()
		# super().save(*args, **kargs)

	def __str__(self):
		return self.item_title
	
	# The get_absolute_url() method sets a canonical URL for the model. 
	# This is required when using the reverse() function. 
	# It is the correct way to refer to a model in templates to avoid hard-coding.
	def get_absolute_url(self):
		return reverse('item_list', args=[str(self.id)])

class Auction(models.Model):
	item_title = models.OneToOneField(
		'Item',
		on_delete=models.CASCADE)
	auction_status = models.CharField(max_length = 25)
	auction_winer = models.CharField(max_length = 25)
	#time_left = models.DateTimeField(verbose_name='Time left to complete')
	
	def __str__(self):
		return str(self.id)
	
	def get_absolute_url(self):
		return reverse('auction_list', args=[str(self.id)])

class Bid(models.Model):
	item_title = models.ForeignKey(
		'Item', 
		on_delete=models.CASCADE)
	bidder = models.CharField(max_length = 25) #? Get it from oAuth
	bid_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Bid')
	bid_timestamp = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
	
	def __str__(self):
		return "%s %s %s" % (self.item_title, self.bidder, bid_price)
	
	def get_absolute_url(self):
		return reverse('bid_list', args=[str(self.id)])