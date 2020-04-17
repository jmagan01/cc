from rest_framework import serializers
from . models import *

class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ItemDetail
		fields = [
			'url','id',
			'auction_id',
			'item_description',
			'item_quantity',
			'item_category',
			'item_condition',
			]
		
class AuctionSerializer(serializers.HyperlinkedModelSerializer):
	item_details = ItemDetailSerializer(source='items', read_only=True)

	class Meta:
		model = Auction
		fields = [
			'url','id',
			'item_name',
			'item_details', #nested serializer
			'is_active',
			'auction_status',
			'ask_price',
			'time_left',
			'expiration_timedate',
			'seller',
			]

class BidSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bid
		fields = [
			'url','id',
			'auction_id',
			'bidder_name',
			'bid_price',
			]