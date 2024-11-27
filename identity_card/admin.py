from django.contrib import admin

from .models import IdentityCard


class IdentityCardAdmin(admin.ModelAdmin):
    pass

admin.site.register(IdentityCard, IdentityCardAdmin)