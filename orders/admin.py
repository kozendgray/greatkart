from django.contrib import admin
from .models import Payment, Order, OrderProduct


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_id', 'payment_method', 'amount_paid', 'status', 'created_at')
    ordering = ('-created_at',)

    #Required
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'full_name', 'email', 'order_total', 'is_ordered')
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'full_name', 'email', 'address']
    inlines = [OrderProductInline]
    


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
