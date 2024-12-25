from import_export import resources
from import_export.admin import ExportMixin, ImportMixin
from django.contrib import admin
from .models import Restaurant, Menu



# Restaurant Import/Export Resource
class RestaurantResource(resources.ModelResource):
    class Meta:
        model = Restaurant
        fields = ('Res_id', 'vendor_name', 'overall_rating', 'total_ratings', 
                  'price_range', 'type', 'max_delivery', 'min_delivery', 
                  'delivery_time', 'location', 'main_location', 'area')

    def get_import_id_fields(self):
        return ['Res_id']  # Use Res_id as the unique identifier during import

# Restaurant Admin Class
class RestaurantAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    resource_class = RestaurantResource
    list_display = ('vendor_name', 'overall_rating', 'total_ratings', 'location', 'price_range')
    search_fields = ('vendor_name', 'location', 'type')

admin.site.register(Restaurant, RestaurantAdmin)


# Menu Import/Export Resource
class MenuResource(resources.ModelResource):
    class Meta:
        model = Menu
        fields = ('Item_id', 'Res_id', 'category', 'item', 'price', 'product_description')
    
    def get_import_id_fields(self):
        return ['Item_id']  # Use Item_id as the unique identifier during import

# Menu Admin Class
class MenuAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    resource_class = MenuResource
    list_display = ('Item_id', 'Res_id', 'category', 'item', 'price', 'product_description')
    search_fields = ('item', 'category', 'Res_id__restaurant_name')
    list_filter = ('category', 'Res_id__vendor_name')

# Register Menu and Restaurant
admin.site.register(Menu, MenuAdmin)