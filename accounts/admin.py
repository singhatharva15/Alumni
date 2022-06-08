from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from accounts.models import Otp, User
from accounts.resources import UserResource


class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'college','batch','course_completed','mobile','career_opportunity','mentor_students','train_students','attend_events', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'first_name', 'last_name', 'mobile', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)
admin.site.register(Otp)
