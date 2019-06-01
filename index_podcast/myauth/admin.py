from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + \
                (('Extra Information', {'fields': ('channelid', )}, ), )

#admin.site.unregister(User)
admin.site.register(User, UserAdmin)