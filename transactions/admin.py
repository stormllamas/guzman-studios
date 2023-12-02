from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['value', 'creation_date']}),
    ]
    # list_display = ('value', 'creation_date')
    # list_editable = ('value',)
    # list_display_links = ('value',)
    list_per_page = 50
    search_fields = ('value',)


admin.site.register(Transaction)
