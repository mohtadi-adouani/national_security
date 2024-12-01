from django.contrib import admin
from .models import PreRequestIDC

# Register your models here.
class PreRequestIDCAdmin(admin.ModelAdmin):
    pass
admin.site.register(PreRequestIDC, PreRequestIDCAdmin)