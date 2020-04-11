from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import filters
from .serializers import ItemSerializer
from .models import Item

# # Testing
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

from django.contrib.auth.models import User

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all().order_by('expiry_date')
	serializer_class = ItemSerializer # This is from step 4.3
	filter_backends = (filters.SearchFilter, )
	search_fields = ['seller']