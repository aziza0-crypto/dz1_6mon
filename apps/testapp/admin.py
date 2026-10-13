from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'role', 'is_verified', 'is_active')
    list_filter = ('role', 'is_verified')
    search_fields = ('email', 'username')

    fieldsets = UserAdmin.fieldsets + (
        ('Личная информация', {
            'fields': ('bio', 'birth_date', 'is_verified', 'role')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {
            'fields': ('role',)
        }),
    ) 