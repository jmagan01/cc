# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'auctions', views.AuctionView)
router.register(r'items', views.ItemDetailView)
router.register(r'bids', views.BidView)

urlpatterns = [
	path('', include(router.urls)),
]
