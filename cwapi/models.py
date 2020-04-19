from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Libraries for data validation
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Other useful libraries
from datetime import datetime
from django.db.models import Max
from django.db.models import Value

# Some generic functions

# Get the record with the maximum bid_price for a specific auction
def get_winner_instance(auction_id):
	auction_data = Bid.objects.filter(auction_id=auction_id)
	max_bid_price = auction_data.aggregate(Max('bid_price'))['bid_price__max']
	winner_instance = Bid.objects.get(bid_price=max_bid_price)
	return winner_instance

# def get_sellers():
	# auction_instance = Auction.objects.filter(auction_id=auction_id)
	# print(auction_instance.seller)
	#return auction_instance.seller

# Create your models here.
class Auction(models.Model):
	"""
	This model holds the key data of the item to be auctioned.
	All items are first created in this model/table.
	"""

	# Validators 
	# def is_in_the_future(value):
		# now = datetime.utcnow()
		# if value <= now:
			# raise ValidationError(_('%(value)s must be a future date and time'), 
				# params = {'value': value},)
			
	def is_positive(value):
		if value <= 0:
			raise ValidationError(_('%(value) must be a positive number'), 
				params = {'value': value},)
	
	# Model Fields
	item_name = models.CharField(
		# Explicit validation, unique, not null, not blank
		unique=True, #unique implies the creation of an index.
		max_length=100,
		verbose_name='Item Title')
		
	ask_price = models.DecimalField(
		max_digits=12,
		decimal_places=2,
		# Explicit validation, positive integer, not null, not blank
		blank=False,
		null=False,
		verbose_name='Starting Price (£)',
		validators = [is_positive])
		
	seller = models.CharField(
		# Explicit validation, not null, not blank
		blank=False,
		null=False,
		max_length=25) #? Get it from oAuth
		
	auction_status = models.CharField(
		# The field will not be displayed in the admin or any other ModelForm
		editable=False,
		max_length=25,
		default="Open")
	
	posted_datetime = models.DateTimeField(
		# Automatically set the field to now when the object is first created
		# The field will not be displayed in the admin or any other ModelForm
		auto_now_add=True,
		editable=False)
	
	expiration_datetime = models.DateTimeField(
		null=False,
		blank=False,)
	
	auction_winner = models.CharField(
		# Explicit validation, not null, not blank
		blank=False,
		null=False,
		max_length=25,
		default="To be confirmed")
	
	purchase_price = models.DecimalField(
		max_digits=12,
		decimal_places=2,
		# Explicit validation, positive integer, not blank
		blank=True,
		null=True,
		default=0,
		verbose_name='Purchase Price (£)',
		validators = [is_positive])
	
	last_update = models.DateTimeField(
		# Automatically set the field to now every time the object is saved
		# The field will not be displayed in the admin or any other ModelForm
		auto_now=True,
		editable=False)
		
	def get_time_delta(self):
		delta = (self.expiration_datetime) - datetime.now()
		return delta
	
	def is_active(self):
		active = self.get_time_delta().total_seconds() > 0
		if not active:
			self.close_auction_and_save()
		return active

	def time_left(self):
		td = self.get_time_delta()
		remaining_time = '{} Days, {} Hours, {} Minutes, {} Seconds'.format(0,0,0,0)
		if td.total_seconds() > 0:
			totalmin, seconds = divmod(td.seconds, 60)
			hour, minutes = divmod(totalmin, 60)
			remaining_time = '{} Days, {} Hours, {} Minutes, {} Seconds'.format(td.days,hour,minutes,seconds)
		return remaining_time
	
	def close_auction(self):
		self.auction_status = "Completed"
		winner = get_winner_instance(self.id)
		self.auction_winner = winner.bidder
		self.purchase_price = winner.bid_price

	def close_auction_and_save(self, *args, **kwargs):
		self.close_auction() # close it, set winner and purchase price
		super(Auction, self).save(*args, **kwargs) #real save
	
	#Metadata
	class Meta:
		unique_together = ('seller', 'id',)

	def __str__(self):
		return 'Auction %s - %s' % (self.id, self.item_name)


class Bid(models.Model):

	def is_positive(value):
		if value <= 0:
			raise ValidationError(_('%(value) must be a positive number'), 
				params = {'value': value},)
				
	# def is_not_seller(value):
		# if name == "mary": #get_item_owner(auction_id):
			# raise ValidationError('Not allowed!')

	# Model fields
	auction_id = models.ForeignKey(
		'Auction', 
		related_name='bids',
		on_delete=models.CASCADE)
		
	bidder = models.CharField(
		# Explicit validation, not null, not blank
		blank=False,
		null=False,
		max_length=25,
		verbose_name='Bidder name',)
		#validators = [is_not_seller,]) #? Get it from oAuth

	bid_price = models.DecimalField(
		max_digits=12,
		decimal_places=2,
		verbose_name='Bid',
		validators = [is_positive,]) #validate vs current_bid_price

	bid_timestamp = models.DateTimeField(
		auto_now_add=True,
		blank=False,)
		
	# Conditional save
	# def save(self, *args, **kwargs):
		# if not is_seller(self.bidder, self.auction_id):
			# super(Auction, self).save(*args, **kwargs) #real save
	
	def __str__(self):
		return 'Bid %s - %s - £ %s - %s' % (self.id, self.bidder, self.bid_price, self.bid_timestamp)


class ItemDetail(models.Model):
	"""
	This model holds additional details about the item to be auctioned.
	None of the fields in this class are essential to complete the auction process.
	"""
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
		#primary_key=True, #django won’t add the automatic id column.
		related_name='item_details',
		on_delete = models.CASCADE)
	
	#owner = Auction.seller
	
	item_description = models.TextField(
		# Field is optional
		blank=True,
		max_length=500,
		verbose_name='Item Description')

	item_quantity = models.PositiveIntegerField(
		blank=False,
		default=1,		
		verbose_name='Quantity')

	item_category = models.CharField(
		max_length=3,
		choices=CATEGORIES,
		verbose_name='Item Category')

	item_condition = models.CharField(
		max_length=1,
		choices=CONDITION_TYPE,
		verbose_name='Condition of the Item')

	def __str__(self):
		return 'Item %s - %s' % (self.id, self.auction_id.item_name)

