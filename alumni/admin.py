from django.contrib import admin
from accounts.models import User
from alumni.models import Career, Opportunities, Events, Applications, EventAttendees

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm

#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'Alumni Details',
#             {
#                 'fields': (
#                     'batch',
#                     'college',
#                     'course_completed',
#                     'mobile',
#                     'certificate',
#                     'career_opportunity',
#                     'mentor_students',
#                     'train_students',
#                     'attend_events',
#                      )
#             }
#         )
#     )
# # Register your models here.
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# class UserPendingCert(BaseUserAdmin):
#     list_display = ['first_name', 'last_name',
#                     'display_name', 'show_certificate']
#     ordering = ('display_name',)


admin.site.register(Career)
admin.site.register(Events)
admin.site.register(EventAttendees)
admin.site.register(Opportunities)
admin.site.register(Applications)

# admin.site.register(UserProxy, UserPendingCert)
