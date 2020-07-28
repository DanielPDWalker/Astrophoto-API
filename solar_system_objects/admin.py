from django.contrib import admin

from solar_system_objects import models


class SolarSystemObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'object_type',
                    'parent_object', 'distance_from_sun_au', 'captured')
    list_display_links = ('name',)
    list_editable = ('captured',)
    search_fields = ('object_type', 'parent_object',
                     'distance_from_sun_au')
    list_per_page = 25


admin.site.register(models.SolarSystemObject, SolarSystemObjectAdmin)
