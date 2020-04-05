from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import Item

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all().order_by('expiry_date')
	serializer_class = ItemSerializer # This is from step 4.3