from django.contrib import admin

from .models import Airline, Flight

# Register your models here.
admin.site.register(Airline)
admin.site.register(Flight)
