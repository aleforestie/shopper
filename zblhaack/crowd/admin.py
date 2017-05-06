from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'ref', 'main_color', 'lesser_color', 'family', 'brand')
	list_filter = ['brand', 'main_color', 'lesser_color', 'family']
	search_fields = ['nom', 'ref']

admin.site.register(Product, ProductAdmin)
