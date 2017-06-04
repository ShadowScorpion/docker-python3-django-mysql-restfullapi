from django.contrib import admin
from .models import Server, OperatingSystem

class ServerAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'os', 'enabled')
    search_fields = ('hostname', 'enabled')
    list_filter = ('hostname', 'enabled')
    save_on_top = True

class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'version')
    search_fields = ('name', 'version')
    list_filter = ('name', 'version')
    save_on_top = True

admin.site.register(Server, ServerAdmin)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
