from django.contrib import admin
from .models import PreRequestIDC, PreRequestPassport

# Register your models here.
class PreRequestIDCAdmin(admin.ModelAdmin):
    pass
admin.site.register(PreRequestIDC, PreRequestIDCAdmin)


class PreRequestPassportAdmin(admin.ModelAdmin):
    pass
admin.site.register(PreRequestPassport, PreRequestPassportAdmin)