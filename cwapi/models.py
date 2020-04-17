from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Auction(models.Model):

	item_name = models.CharField(
		max_length = 100,
		verbose_name = 'Item Title')
	ask_price = models.PositiveIntegerField(verbose_name = 'Starting Price (£)')
	seller = models.CharField(max_length = 25) #? Get it from oAuth
	posted_timedate = models.DateTimeField(
		auto_now_add = True, 
		editable = False)
	expiration_timedate = models.DateTimeField()
	#is_active = models.BooleanField()
	auction_status = models.CharField(
		max_length = 25, 
		default = "Open to offers")
	auction_winner = models.CharField(
		max_length = 25,
		editable = False,
		blank = False,
		null = True,)
	
	def get_time_delta(self):
		return self.expiration_timedate - datetime.now()
	
	def is_active(self):
		return self.get_time_delta().total_seconds() > 0
		
	def update_auction_status(self):
		return "Open to offers" if self.is_active() else "Completed"

	def time_left(self):
		td = self.get_time_delta()
		remaining_time = '{} Days, {} Hours, {} Minutes, {} Seconds'.format(0,0,0,0)
		if td.total_seconds() > 0:
			totalmin, seconds = divmod(td.seconds, 60)
			hour, minutes = divmod(totalmin, 60)
			remaining_time = '{} Days, {} Hours, {} Minutes, {} Seconds'.format(td.days,hour,minutes,seconds)
		return remaining_time
	
	# def	update_auction(self, bid_price, bidder_name):
		# if bid_price > self.current_bid_price:
			# self.best_bidder_name = bidder_name 
			# self.current_bid_price = bid_price
		# return self.best_bidder_name, self.current_bid_price
	
	def close_auction(self):
		seld.auction_status = "Completed"
		# self.auction_winner = get name of best bidder from Bid table
		# see https://stackoverflow.com/questions/844591/how-to-do-select-max-in-django
	
	def save(self, *args, **kwargs):
		# check if the auction is still open before saving data
		if not self.is_active:
			# deadline has passed, close the auction
			self.close_auction()
		else:
			print("auction still active")
			# auction still open, save the data.
		super(Auction, self).save(*args, **kwargs) #Real save
	
	#Metadata
	class Meta:
		ordering = ["-posted_timedate"]

	def __str__(self):
		return 'Auction %s - %s' % (self.id, self.item_name)


class Bid(models.Model):
	auction_id = models.ForeignKey(
		'Auction', 
		on_delete = models.CASCADE)
	bidder_name = models.CharField(max_length = 25) #? Get it from oAuth
	bid_price = models.DecimalField(max_digits = 6, decimal_places = 2, verbose_name ='Bid')
	bid_timestamp = models.DateTimeField(auto_now_add = True, blank = False, editable = False)
	
	def save(self, *args, **kwargs):
		if Bid.auction_id.is_active:
			#Save bid in database
			super(Bid, self).save(*args, **kwargs) #Real save
		else: 
			raise Exception('The auction is closed. The following bid has not been accepted: {}'.format(self.bid_price))
		
	
	def __str__(self):
		return "%s %s %s" % (self.id, self.bidder, bid_price)
		
		
		
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
		verbose_name ='Item Category')
	item_condition = models.CharField(
		max_length = 1,
		choices = CONDITION_TYPE,
		verbose_name = 'Condition of the Item')

	def __str__(self):
		return 'Item %s - %s' % (self.id, self.auction_id.item_name)
