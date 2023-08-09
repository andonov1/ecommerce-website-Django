from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

    ordering = ('first_name',)

    list_display = ('email', 'first_name', 'last_name', 'is_staff')

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    search_fields = ('email', 'first_name', 'last_name')


admin.site.register(CustomUser, UserAdmin)
