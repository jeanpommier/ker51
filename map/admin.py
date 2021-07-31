from django.contrib.gis import admin

from .models import Person

class PersonAdmin(admin.OSMGeoAdmin):
    # default_lon = 300000
    # default_lat = 6000000
    default_lon = 2
    default_lat = 42
    default_zoom = 3
    list_display = ('names', 'fulladdress', 'phones', 'emails', 'comments')

admin.site.register(Person, PersonAdmin)