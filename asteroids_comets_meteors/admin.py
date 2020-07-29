from django.contrib import admin

from asteroids_comets_meteors import models


class AsteroidCometMeteorObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'object_type',
                    'captured', 'capture_date')
    # We dont show the slug in the admin view.
    # Its auto generated on object creation, and guarenteed unique.
    exclude = ('slug',)
    list_display_links = ('name', 'scientific_name')
    list_editable = ('captured',)
    search_fields = ('object_type',)
    list_per_page = 25


admin.site.register(models.AsteroidCometMeteorObject,
                    AsteroidCometMeteorObjectAdmin)
