from django.contrib.gis import admin

from .models import Hivernant, Phone, Email

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1

class HivernantAdmin(admin.OSMGeoAdmin):
    default_lon = 300000
    default_lat = 6000000
    # default_lon = 2
    # default_lat = 42
    default_zoom = 2
    list_display = ('names', 'fulladdress', 'comments')
    inlines = [PhoneInline, EmailInline]

admin.site.register(Hivernant, HivernantAdmin)