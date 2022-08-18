from django.contrib import admin
from alumni.models import Career, Opportunities, Events


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

admin.site.register(Events)
admin.site.register(Opportunities)
admin.site.register(Career)
