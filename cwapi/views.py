from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import filters
from .serializers import *
from .models import *

class AuctionView(viewsets.ModelViewSet):
	queryset = Auction.objects.all()
	serializer_class = AuctionSerializer

class ItemView(viewsets.ModelViewSet):
	queryset = Item.objects.all().order_by('expiry_date')
	serializer_class = ItemSerializer # This is from step 4.3
	filter_backends = (filters.SearchFilter, )
	search_fields = ['seller']
	
class BidView(viewsets.ModelViewSet):
	queryset = Bid.objects.all().order_by('bid_amount')
	serializer_class = BidSerializer