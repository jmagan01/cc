from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ItemDetail)
admin.site.register(Auction)
admin.site.register(Bid)