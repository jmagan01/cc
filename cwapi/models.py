from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Auction(models.Model):
	item_title = models.OneToOneField(
		'Item',
		on_delete=models.CASCADE)
	auction_status = models.CharField(max_length = 25)
	auction_winer = models.CharField(max_length = 25)
	#time_left = models.DurationField(verbose_name='Time left to complete')
	
	def __str__(self):
		return str(self.id)
	
	def get_absolute_url(self):
		return reverse('auction_list', args=[str(self.id)])

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
	item_title = models.CharField(max_length = 100,verbose_name='Item Title')
	starting_price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name='Starting Price')
	quantity = models.IntegerField(verbose_name='Quantity')
	condition = models.CharField(max_length = 1,choices=CONDITION_TYPE,verbose_name='Condition of the Item')
	description = models.CharField(max_length = 255,verbose_name='Item Description')
	category = models.CharField(max_length = 3,choices=CATEGORIES,verbose_name='Item Category')
	date_posted = models.DateTimeField(auto_now_add=True, blank=True)
	expiry_date = models.DateTimeField()
	seller = models.CharField(max_length = 25) #? Get it from oAuth

	def __str__(self):
		return self.item_title
	
	# The get_absolute_url() method sets a canonical URL for the model. 
	# This is required when using the reverse() function. 
	# It is the correct way to refer to a model in templates to avoid hard-coding.
	def get_absolute_url(self):
		return reverse('item_list', args=[str(self.id)])
		
class Bid(models.Model):
	item_title = models.ForeignKey(
		'Item', 
		on_delete=models.CASCADE)
	bidder = models.CharField(max_length = 25) #? Get it from oAuth
	bid_amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Bid')
	bid_timestamp = models.DateTimeField(auto_now_add=True, blank=True)
	
	def __str__(self):
		return "%s %s %s" % (self.item_title, self.bidder, bid_amount)
	
	def get_absolute_url(self):
		return reverse('bid_list', args=[str(self.id)])