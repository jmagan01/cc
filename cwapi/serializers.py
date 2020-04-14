from rest_framework import serializers
from .models import Bid, ItemDetail, Auction

class AuctionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Auction
		fields = [
			'url',
			'id',
			'item_title',
			'starting_price',
			'seller',
			'expiration_timedate',
		]
		depth = 1

class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ItemDetail
		fields = [
			'url',
			'id',
			'category',
			'condition',
			'quantity',
			'description',
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
		fields = ['url','id','item_title','bidder','bid_price','bid_timestamp']