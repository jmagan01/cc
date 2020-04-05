# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'item', views.ItemViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
