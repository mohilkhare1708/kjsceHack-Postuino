from django.contrib import admin
from mainapp import models


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'email', 'phone', 'height_cms')
    list_display_links = ('id', 'user', 'full_name',
                          'email', 'phone', 'height_cms')
    search_fields = ('id', 'full_name')
    list_per_page = 20


admin.site.register(models.Profile, ProfileAdmin)
