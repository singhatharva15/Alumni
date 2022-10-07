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

    fieldsets = ()

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = []
    list_filter = []
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=False)

    def has_change_permission(self, request, obj=None):
        return (request.user.is_superuser or request.user.is_staff)

    def has_delete_permission(self, request, obj=None):
        return (request.user.is_superuser or request.user.is_staff)

    def has_add_permission(self, request):
        return (request.user.is_superuser or request.user.is_staff)

    def has_view_permission(self, request, obj=None):
        return (request.user.is_superuser or request.user.is_staff)

    def has_module_permission(self, request):
        return (request.user.is_superuser or request.user.is_staff)

    def changelist_view(self, request, extra_context=None):
        if not request.user.is_superuser:
            self.list_display = ['email', 'first_name', 'last_name',
                                 'mobile', 'display_name', 'show_certificate']
            self.list_filter = []
            self.fieldsets = (
                (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'display_name', 'college', 'batch', 'course_completed', 'course_complete_start', 'course_complete_end',
                                   'mobile', 'show_certificate', 'career_opportunity', 'mentor_students', 'train_students', 'attend_events', 'last_login')}),
            )
        else:
            self.list_display = ['email', 'first_name', 'last_name',
                                 'mobile', 'is_staff', 'last_login']
            self.list_filter = ('is_staff', 'is_superuser',
                                'is_active', 'groups')
            self.fieldsets = (
                (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'display_name', 'college', 'batch', 'course_completed', 'course_complete_start', 'course_complete_end',
                                   'mobile', 'show_certificate', 'career_opportunity', 'mentor_students', 'train_students', 'attend_events', 'last_login')}),
                ('Permissions', {'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )}),
            )
        return super(UserAdmin, self).changelist_view(request, extra_context)


admin.site.register(User, UserAdmin)
admin.site.register(Otp)
