from django.contrib import admin
from .models import ShippingUser, Shipment, ShippingMethod






# Register the Todo model
# Register the ShippingUser model
@admin.register(ShippingUser)
class ShippingUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_business_account', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_business_account', 'created_at')

# Register the Shipment model
@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'sender', 'recipient_name', 'status', 'created_at')
    search_fields = ('tracking_number', 'recipient_name', 'sender__username')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)

# Register the ShippingMethod model
@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'carrier', 'cost', 'created_at')
    search_fields = ('name', 'carrier')
    list_filter = ('carrier',)