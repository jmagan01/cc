from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('title')
	serializer_class = ProductSerializer # This is from step 4.3
