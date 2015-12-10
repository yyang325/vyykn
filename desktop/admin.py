from django.contrib import admin

from alertDevice.models import AlertDevice
from desktop.models import DeskTop
# Register your models here.

class DeskTopAdmin(admin.ModelAdmin):
    list_display=["desktop_id", "__str__"]

admin.site.register(DeskTop)
