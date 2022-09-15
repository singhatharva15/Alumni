from faulthandler import disable
import re

from accounts.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Field, Layout, Row, Submit
from django import forms

from .models import Career


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'college',
            'course_completed',
            'email',
            'mobile',
            'batch',
            'career_opportunity',
            'mentor_students',
            'train_students',
            'attend_events'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'disabled': True}),
            'batch': forms.TextInput(attrs={'disabled': True}),
            'last_name': forms.TextInput(attrs={'disabled': True}),
            'college': forms.TextInput(attrs={'disabled': True}),
            'course_completed': forms.TextInput(attrs={'disabled': True}),
            'email': forms.TextInput(attrs={'disabled': False}),
            'mobile': forms.TextInput(attrs={'disabled': False}),
            'career_opportunity': forms.CheckboxInput(attrs={'disabled': True}),
            'mentor_students': forms.CheckboxInput(attrs={'disabled': True}),
            'train_students': forms.CheckboxInput(attrs={'disabled': True}),
            'attend_events': forms.CheckboxInput(attrs={'disabled': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h3 class="mb-3">Update Profile</h3>'),
            Row(
                Column(Field('first_name'), css_class='col-sm-12 col-md-6'),
                Column(Field('last_name'), css_class='col-sm-12 col-md-6',),
                Column(Field('email'), css_class='col-sm-12 col-md-6'),
                Column(Field('mobile'), css_class='col-sm-12 col-md-6'),
                
            ),
            Row(
                Column(Field('batch'), css_class='col-sm-12 col-md-2'),
                Column(Field('college'), css_class='col-sm-12 col-md-10'),
                css_class='row'
            ),
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
                "Phone number must be 10 digits.")


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
