from rest_framework import serializers
from .models import Bid, ItemDetail, Auction

class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ItemDetail
		fields = [
			'url',
			'id',
			'item_name',
			'category',
			'condition',
			'quantity',
			'description',
		]
		
class AuctionSerializer(serializers.HyperlinkedModelSerializer):
	item_details = ItemDetailSerializer(source='items', read_only=True)
	class Meta:
		model = Auction
		fields = [
			'url',
			'id',
			'item_name',
			'item_details', #nested serializer
			'ask_price',
			'seller',
			'expiration_timedate',
		]
		#depth = 1

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
		fields = ['url','id','item_title','bidder','bid_price','bid_timestamp']