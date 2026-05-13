from django.contrib import admin
from .models import Portafolio, Profile


class PortafolioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Portafolio, PortafolioAdmin)
admin.site.register(Profile, ProfileAdmin)