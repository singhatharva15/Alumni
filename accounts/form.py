from django import forms
from random import randint

from accounts.models import User, Otp
from utils.sendmail import send_otp_to_email


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