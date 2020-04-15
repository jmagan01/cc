from rest_framework import serializers
from . models import *

class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ItemDetail
		fields = [
			'url',
			'id',
			'auction_id',
			'item_description',
			'item_quantity',
			'item_category',
			'item_condition',
		]
		
class AuctionSerializer(serializers.HyperlinkedModelSerializer):
	item_details = ItemDetailSerializer(source='items', read_only=True)
	#time_left = serializers.DateField(required=False)

	class Meta:
		model = Auction
		fields = [
			'url',
			'id',
			'auction_status',
			'item_name',
			'ask_price',
			'item_details', #nested serializer
			'seller',
			'expiration_timedate',
			#'time_left',
		]

class BidSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bid
		fields = ['url','id',
			'item_id','item_name','bidder','bid_price','bid_timestamp']