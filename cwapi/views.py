from django.shortcuts import render

# Create your views here.
from django_filters import rest_framework as filters
from rest_framework import viewsets
#from rest_framework import filters
from . serializers import *
from . models import *

#from django_filters.rest_framework import DjangoFilterBackend

class ExpirationFilter(filters.FilterSet):
	expiration_gte = filters.DateTimeFilter(
		field_name ="expiration_timedate", 
		lookup_expr='gte')
	class Meta:
		model = Auction
		fields = ['seller', 'expiration_gte']

class AuctionView(viewsets.ModelViewSet):
	queryset = Auction.objects.all().order_by('-expiration_timedate')
	serializer_class = AuctionSerializer
	#filter_backends = [filters.SearchFilter, ]#, DjangoFilterBackend,) #do not delete the comma
	#search_fields = ['seller', ]
	#filterset_fields = ['expiration_timedate', 'auction_status']
	filter_class = ExpirationFilter

class ItemDetailView(viewsets.ModelViewSet):
	queryset = ItemDetail.objects.all()
	serializer_class = ItemDetailSerializer # This is from step 4.3
	
class BidView(viewsets.ModelViewSet):
	queryset = Bid.objects.all().order_by('bid_price')
	serializer_class = BidSerializer