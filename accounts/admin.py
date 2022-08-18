from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import Otp, User
from accounts.resources import UserResource
from accounts.forms import UserCreationForm, UserChangeForm


class UserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

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


    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    # def has_delete_permission(self, request, obj=None):
    #     return self._allow_edit(obj)

    # def has_add_permission(self, request):
    #     return True

    # def get_actions(self, request):
    #     actions = super(UserAdmin, self).get_actions(request)
    #     if request.user.is_staff:
    #         del actions
    #     return actions

    def has_view_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

admin.site.register(User, UserAdmin)
admin.site.register(Otp)
