from rest_framework import serializers
from .models import Bid, ItemDetail, Auction

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
			#'item_id',
			#'item_name',
		]
		
class AuctionSerializer(serializers.HyperlinkedModelSerializer):
	item_details = ItemDetailSerializer(source='items', read_only=True)
	class Meta:
		model = Auction
		fields = [
			'url',
			'id',
			'item_name',
			'ask_price',
			'item_details', #nested serializer
			'seller',
			'expiration_timedate',
		]

# class AuctionDetailSerializer(serializers.HyperlinkedModelSerializer):
	# item_details = ItemDetailSerializer(read_only=True)
	# class Meta:
		# model = Auction
		# fields = [
			# 'url',
			# 'id',
			# 'starting_price',
			# 'seller',
			# 'status',
			# 'posted_timedate',
			# 'expiration_timedate',
			# 'time_left',
			# 'item_title',
			# 'item_details',
		# ]
		# depth = 1

class BidSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bid
		fields = ['url','id',
			'item_id','item_title','bidder','bid_price','bid_timestamp']