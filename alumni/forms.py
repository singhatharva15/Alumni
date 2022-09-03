from django import forms
from .models import Career
from accounts.models import User
import re
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, HTML, Submit


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'college',
            'course_completed',
            'mobile',
            'career_opportunity',
            'mentor_students',
            'train_students',
            'attend_events'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h3 class="mt-4 mb-3">Update Profile</h3>'),
            Row(
                Column(Field('first_name'), css_class='col-sm-12 col-md-4'),
                Column(Field('last_name'), css_class='col-sm-12 col-md-4',),
                Column(Field('mobile'), css_class='col-sm-12 col-md-4'),
                css_class='row'
            ),
            'college',
            'course_completed',
            Row(
                Column(Field('career_opportunity'),
                       css_class='col-sm-6 col-md-3'),
                Column(Field('mentor_students'),
                       css_class='col-sm-6 col-md-3',),
                Column(Field('train_students'), css_class='col-sm-6 col-md-3'),
                Column(Field('attend_events'), css_class='col-sm-6 col-md-3'),
                css_class='row'
            ),
            HTML('<hr>'),
            Submit('update-profile-form-submit',
                   'Update Profile', css_class="btn btn-primary")
        )

    def clean(self):
        cleaned_data = super().clean()
        mobile = cleaned_data.get('mobile')
        if len(re.findall("^\d{10}$", mobile)) == 0:
            raise forms.ValidationError(
                "Phone number must be entered in the format: '+999999999'. Up to 15 digits is allowed.")


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ('present', 'organization', 'position', 's_date', 'e_date')

        widgets = {
            's_date': forms.DateInput(attrs={'type': 'date'}),
            'e_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'position',
            'organization',
            Row(
                Column(Field('s_date'), css_class='col-sm-12 col-md-6'),
                Column(Field('e_date'), 'present',
                       css_class='col-sm-12 col-md-6'),
                css_class='row'
            ),
            HTML('<div class="text-right">'),
            HTML('<hr />'),
            Submit('add-exp-form-submit', 'Submit',
                   css_class="btn btn-primary"),
            HTML('</div>'),
        )

    # Logic for raising error if end_date < start_date
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("s_date")
        end_date = cleaned_data.get("e_date")
        if end_date < start_date:
            raise forms.ValidationError(
                "End date should be greater than start date.")
