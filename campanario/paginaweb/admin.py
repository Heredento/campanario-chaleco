from django.contrib import admin
from paginaweb.models import auth_code, events_list, events_files, ClockInformation, events_backups

class AuthCode(admin.ModelAdmin):
    pass
class EventsList(admin.ModelAdmin):
    pass
class EventsFiles(admin.ModelAdmin):
    pass
class EventsBackups(admin.ModelAdmin):
    pass
class ClockInfo(admin.ModelAdmin):
    pass


admin.site.register(auth_code, AuthCode)
admin.site.register(events_list, EventsList)
admin.site.register(events_files, EventsFiles)
admin.site.register(events_backups, EventsBackups)
admin.site.register(ClockInformation, ClockInfo)

