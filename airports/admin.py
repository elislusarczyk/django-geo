from django.contrib.gis import admin
from .models import Airport

admin.site.register(Airport, admin.ModelAdmin)