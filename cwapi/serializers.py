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

class AuctionDataSerializer(serializers.ModelSerializer):
	class Meta:
			model = Auction
			fields = [
				'url', 
				'id',
				'is_active',
				'seller',
				]
	
class BidSerializer(serializers.ModelSerializer):
	auctiondata = AuctionDataSerializer(
		source='bids',
		required=False, #Non-compulsory information
		read_only=True
		)

	class Meta:
		model = Bid
		fields = [
			'url','id',
			'auction_id',
			'auctiondata',
			'bid_price',
			'bidder',
			]
		#read_only_fields = [
		#	'auction_data',
		#	]
		
	# def validate_date_of_birth(self, dob):
        # today = date.today()
        # age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        # if (not(20 < age < 30)):
            # raise serializers.ValidationError("You are no eligible for the job")
        # return dob

class AuctionSerializer(serializers.HyperlinkedModelSerializer):
	item_detail = ItemDetailSerializer(
		source='item_details',
		required=False, #Non-compulsory information
		read_only=True)
		
	bid_details = BidSerializer(
		source='bids',
		many=True,
		required=False, #Non-compulsory information
		read_only=True)

	class Meta:
		model = Auction
		fields = [
			'url','id',
			'item_name',
			'item_detail', #Nested serializer
			'is_active',
			'auction_status',
			'time_left',
			'expiration_timedate',
			'seller',
			'ask_price',
			'auction_winner',
			'bid_details',
			]
		read_only_fields = [
			'is_active',
			'auction_status',
			'time_left',
			'auction_winner',
			]
