from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		#fields = ('item_id','item_title','date_posted','quantity',
		#'condition','description','category','expiry_date','seller')
		fields = '__all__'
		
class AuctionSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Auction
		fields = (
			'time_left','item_id','item_title', 'quantity', 'condition',
			'description','category','seller')
