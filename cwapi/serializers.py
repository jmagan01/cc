from rest_framework import serializers
from .models import Bid, Item, Auction
from datetime import datetime, timedelta

class AuctionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Auction
		fields = ('url', 'id', 'item_title', 'auction_status')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = ('url','id','item_title','starting_price','date_posted',
		'quantity', 'condition','description','category','expiry_date','seller',
		'time_left')
		
class BidSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bid
		fields = ('url','id','item_title','bidder','bid_price','bid_timestamp')