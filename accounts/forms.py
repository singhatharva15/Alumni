from django import forms
from random import randint
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User, Otp
from utils.sendmail import send_otp_to_email


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class EmailForm(forms.Form):
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        try:
            user = User.objects.get(email=email)
            otp_code = randint(100000, 999999)
            otp_obj, created = Otp.objects.get_or_create(user=user)
            otp_obj.otp = str(otp_code)
            otp_obj.is_valid = True
            otp_obj.save()
            res = send_otp_to_email(email, f"{user.first_name} {user.last_name}", otp_code)
            if res.status_code != 200:
                raise Exception("Email was not sent!")
        except User.DoesNotExist:
            raise forms.ValidationError("You are not registered please contact admin!")
        except Exception as e:
            raise forms.ValidationError("Something went wrong! Plese try again.")



class OtpForm(forms.Form):
    otp = forms.CharField()