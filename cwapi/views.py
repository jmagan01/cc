from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets

from . serializers import *
from . models import *


# Custom filters
class AuctionFilters(filters.FilterSet):
	expiration_gte = filters.DateTimeFilter(
		field_name ="expiration_datetime", 
		lookup_expr='gte')
	class Meta:
		model = Auction
		fields = ['seller', 'auction_status', 'expiration_gte']

class BidFilters(filters.FilterSet):
	bid_price_gte = filters.NumberFilter(
		field_name ="bid_price", 
		lookup_expr='gte')
	class Meta:
		model = Bid
		fields = ['auction_id','bidder','bid_price_gte']

# Create your views here.
class AuctionView(viewsets.ModelViewSet):
	queryset = Auction.objects.all().order_by('-auction_status','expiration_datetime')
	serializer_class = AuctionSerializer
	filter_class = AuctionFilters

class ItemDetailView(viewsets.ModelViewSet):
	queryset = ItemDetail.objects.all()
	serializer_class = ItemDetailSerializer
	
class BidView(viewsets.ModelViewSet):
	queryset = Bid.objects.all().order_by('-bid_price')
	serializer_class = BidSerializer
	filter_class = BidFilters

	# def validate(self, data):
		# if self.context['request'].bidder == data['auction_id'].seller:
			# raise ValidationError(u"Bidder & owner must be different")
		# return data