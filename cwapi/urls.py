# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'auctions', views.AuctionViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
