from rest_framework import serializers
from . models import *
from datetime import datetime

class ItemDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemDetail
		fields = [
			'url', 'id',
			'auction_id',
			'item_description',
			'item_quantity',
			'item_category',
			'item_condition',
			]

class BidSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bid
		fields = [
			'url','id',
			'auction_id',
			'bid_price',
			'bidder',
			]

class AuctionSerializer(serializers.HyperlinkedModelSerializer):
	
	item_detail = ItemDetailSerializer(
		source='item_details',
		required=False, #Non-compulsory information
		read_only=True)
		
	# bid_activity = BidSerializer(
		# source='bids',
		# many=True,
		# required=False, #Non-compulsory information
		# read_only=True)

	class Meta:
		model = Auction
		fields = [
			'url','id',
			'item_name',
			'item_detail', #Nested serializer
			'seller',
			'ask_price',
			'is_active',
			'auction_status',
			'expiration_datetime',
			'time_left',
			'auction_winner',
			'purchase_price',
			#'bid_activity', #Nested serializer
			]
		read_only_fields = [
			'is_active',
			'auction_status',
			'time_left',
			'auction_winner',
			'purchase_price',
			]