from rest_framework import serializers
from .models import Bid, Item, Auction

class AuctionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Auction
		fields = ('url', 'id', 'item_title', 'auction_status')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = ('url','id','item_title','starting_price','date_posted',
		'quantity', 'condition','description','category','expiry_date','seller')
		
class BidSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bid
		fields = ('url','id','item_title','bidder','bid_amount','bid_timestamp')