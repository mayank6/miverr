from django.contrib import admin
from .models import Gig,purchase,review
# Register your models here.

admin.site.register(Gig)
admin.site.register(purchase)
admin.site.register(review)
