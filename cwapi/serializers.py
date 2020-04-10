from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = ('item_id','item_title','date_posted','quantity','condition','description','category','expiry_date','seller')