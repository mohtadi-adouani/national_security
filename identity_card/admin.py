from django.contrib import admin

from .models import IdentityCard, Passport


class IdentityCardAdmin(admin.ModelAdmin):
    pass
admin.site.register(IdentityCard, IdentityCardAdmin)

class PassportAdmin(admin.ModelAdmin):
    pass
admin.site.register(Passport, PassportAdmin)