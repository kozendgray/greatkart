from django.contrib import admin
from .models import Payment, Order, OrderProduct


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_id', 'payment_method', 'amount_paid', 'status', 'created_at')
    ordering = ('-created_at',)

    #Required
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    



admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order)
admin.site.register(OrderProduct)