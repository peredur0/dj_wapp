from django.contrib import admin
from listings.models import Band, Listing
# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')     # ce que l'on veut afficher dans la liste admin

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'categorie', 'sold')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)

