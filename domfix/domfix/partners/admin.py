from django.contrib import admin

from domfix.partners.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
