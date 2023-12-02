from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['price', 'creation_date']}),
    ]
    list_display = ('price', 'creation_date',)
    list_editable = ('creation_date',)
    # list_display_links = ('price',)
    list_per_page = 50
    # search_fields = ('price',)


admin.site.register(Booking, BookingAdmin)
