from django.contrib import admin
from .models import Product, FavoriteColor, FavoriteBrand, FavoriteFamily

class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'ref', 'main_color', 'lesser_color', 'family', 'brand')
	list_filter = ['brand', 'main_color', 'lesser_color', 'family']
	search_fields = ['nom', 'ref']

class ColorAdmin(admin.ModelAdmin):
	list_display = ('pk', 'red', 'blue', 'black', 'white')

class BrandAdmin(admin.ModelAdmin):
	list_display = ('pk', 'hype_brand', 'alf_brand', 'annick_brand')

class FamilyAdmin(admin.ModelAdmin):
	list_display = ('pk', 't_shirt', 'jacket', 'sport_shoe', 'pants')

admin.site.register(Product, ProductAdmin)
admin.site.register(FavoriteColor, ColorAdmin)
admin.site.register(FavoriteBrand, BrandAdmin)
admin.site.register(FavoriteFamily, FamilyAdmin)
