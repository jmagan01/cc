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

	item_title = models.CharField(
		max_length = 100,
		verbose_name = 'Item Title')
	starting_price = models.DecimalField(
		max_digits = 6, 
		decimal_places = 2,
		verbose_name = 'Starting Price')
	seller = models.CharField(max_length = 25) #? Get it from oAuth
	posted_timedate = models.DateTimeField(
		auto_now_add=True, 
		editable=False)
	expiration_timedate = models.DateTimeField()
	status = models.PositiveSmallIntegerField(
		choices=STATUS_CHOICES,
		default=STATUS_ACTIVE)
	
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
	def status(self):
		td_sec = self.get_time_delta().total_seconds()
		return Auction.STATUS_ACTIVE if td_sec > 0 else Auction.STATUS_CLOSED
	
	def get_time_delta(self):
		return -1*(datetime.now() - self.expiration_timedate)
	
	#Metadata
	class Meta:
		ordering = ["-posted_timedate"]

	def __str__(self):
		return '%s' % (self.item_title)

		
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
	item_title = models.OneToOneField(
		'Auction',
		on_delete = models.CASCADE)
	category = models.CharField(
		max_length = 3,
		choices = CATEGORIES,
		verbose_name='Item Category')
	condition = models.CharField(
		max_length = 1,
		choices = CONDITION_TYPE,
		verbose_name = 'Condition of the Item')
	quantity = models.IntegerField(verbose_name='Quantity')
	description = models.TextField(verbose_name='Item Description')

	def __str__(self):
		return '%s' % (self.item_title)

class Bid(models.Model):
	item_title = models.ForeignKey(
		'Auction', 
		on_delete=models.CASCADE)
	bidder = models.CharField(max_length = 25) #? Get it from oAuth
	bid_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Bid')
	bid_timestamp = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
	
	def __str__(self):
		return "%s %s %s" % (self.item_title, self.bidder, bid_price)