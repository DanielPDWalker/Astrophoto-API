from django.contrib import admin

from messier_objects import models


class MessierObjectAdmin(admin.ModelAdmin):
    list_display = ('messier_number', 'name', 'object_type',
                    'constellation', 'captured', 'capture_date')
    list_display_links = ('messier_number', 'name')
    list_editable = ('captured',)
    search_fields = ('object_type', 'constellation',
                     'apparent_magnitude')
    list_per_page = 25


admin.site.register(models.MessierObject, MessierObjectAdmin)
