from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import string
import random

# Create your models here.
class Auction(models.Model):
	STATUS_CLOSED, STATUS_ACTIVE = range(2)
	STATUS_CHOICES = (
		(STATUS_CLOSED, 'Closed'), 
		(STATUS_ACTIVE, 'Active'))

	item_name = models.CharField(
		max_length = 100,
		verbose_name = 'Item Title')
	ask_price = models.PositiveIntegerField(verbose_name = 'Starting Price')
	seller = models.CharField(max_length = 25) #? Get it from oAuth
	posted_timedate = models.DateTimeField(
		auto_now_add = True, 
		editable = False)
	expiration_timedate = models.DateTimeField()
	auction_status = models.PositiveSmallIntegerField(
		choices = STATUS_CHOICES,
		default = STATUS_ACTIVE)
	
	@property
	def time_left(self):
		td = self.get_time_delta()
		remaining_time = '{} Days, {} Hours, {} Minutes, {} Seconds'.format(0,0,0,0)
		if td.total_seconds() > 0:
			totalmin, seconds = divmod(td.seconds, 60)
			hour, minutes = divmod(totalmin, 60)
			remaining_time = '{} Days, {} Hours, {} Minutes, {} Seconds'.format(td.days,hour,minutes,seconds)
		return remaining_time
	
	@property
	def auction_status(self):
		td_sec = self.get_time_delta().total_seconds()
		return Auction.STATUS_ACTIVE if td_sec > 0 else Auction.STATUS_CLOSED
	
	def get_time_delta(self):
		return -1*(datetime.now() - self.expiration_timedate)
	
	#Metadata
	class Meta:
		ordering = ["-posted_timedate"]

	def __str__(self):
		return 'Auction %s - %s' % (self.id, self.item_name)

		
class ItemDetail(models.Model):
	CONDITION_TYPE = (
		('N', 'New'),
		('U', 'Used'))
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
		('TOY', 'Toys'))
	auction_id = models.OneToOneField(
		'Auction',
		 related_name = 'items', 
		on_delete = models.CASCADE)
	item_description = models.TextField(verbose_name='Item Description')
	item_quantity = models.IntegerField(verbose_name='Quantity')
	item_category = models.CharField(
		max_length = 3,
		choices = CATEGORIES,
		verbose_name='Item Category')
	item_condition = models.CharField(
		max_length = 1,
		choices = CONDITION_TYPE,
		verbose_name = 'Condition of the Item')

	def __str__(self):
		return 'Item %s - %s' % (self.id, self.auction_id.item_name)

class Bid(models.Model):
	item_id = models.ForeignKey(
		'Auction', 
		on_delete=models.CASCADE)
	bidder = models.CharField(max_length = 25) #? Get it from oAuth
	bid_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Bid')
	bid_timestamp = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
	
	def __str__(self):
		return "%s %s %s" % (self.id, self.bidder, bid_price)