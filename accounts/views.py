from django.shortcuts import redirect, render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages


from accounts.forms import EmailForm, OtpForm
from accounts.models import User, Otp


def send_otp(request):
    if request.POST:
        form = EmailForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            print(email)
            request.session['email'] = email
            return redirect('verify_otp')
        return render(request, 'registration/login.html', {"form": form})
    else:
        form = EmailForm()
    return render(request, 'registration/login.html', {"form": form})


def verify_otp(request):
    if request.POST:
        form = OtpForm(request.POST)

        email = request.session.get('email')

        if email is None:
            messages.error(
                request, message="Something went wrong! Plese try again.")
            return redirect('send_otp')

        if form.is_valid():
            otp_code = form.cleaned_data['otp']
            user = User.objects.get(email=email)

            if user is None:
                messages.error(
                    request, message="You are not registered please contact admin!")
                return redirect('send_otp')

            otp_obj = Otp.objects.get(user=user)

            if otp_code != otp_obj.otp:
                messages.error(
                    request, message="OTP didn't match please try again.")
                return redirect('verify_otp')

            login(request, user)
            otp_obj.is_valid = False
            otp_obj.save()
            del request.session['email']
            return redirect('profile')

        return render(request, 'registration/verify_otp.html', {"form": form})
    else:
        email = request.session.get('email')
        if email is None:
            messages.error(
                request, message="Something went wrong! Plese try again.")
            return redirect('send_otp')

        form = OtpForm()
    return render(request, 'registration/verify_otp.html', {"form": form})
