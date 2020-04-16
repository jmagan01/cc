from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import filters
from . serializers import *
from . models import *

from url_filter.integrations.drf import DjangoFilterBackend

class AuctionView(viewsets.ModelViewSet):
	queryset = Auction.objects.all().order_by('-expiration_timedate')
	serializer_class = AuctionSerializer
	filter_backends = (filters.SearchFilter, DjangoFilterBackend,) #do not delete the comma
	search_fields = ['seller', ]
	#filter_backends = [DjangoFilterBackend]
	#filter_fields = ('is_active', )

class ItemDetailView(viewsets.ModelViewSet):
	queryset = ItemDetail.objects.all()
	serializer_class = ItemDetailSerializer # This is from step 4.3
	
class BidView(viewsets.ModelViewSet):
	queryset = Bid.objects.all().order_by('bid_price')
	serializer_class = BidSerializer