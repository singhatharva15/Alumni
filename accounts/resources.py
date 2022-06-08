from dataclasses import fields
from import_export import resources
from accounts.models import User

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = (
            'email', 
            'first_name', 
            'last_name', 
            'college', 
            'batch', 
            'course_completed', 
            'mobile', 
            'career_opportunity', 
            'mentor_students', 
            'train_students', 
            'attend_events',
            'id'
        )