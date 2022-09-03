import os
import requests


def send_otp_to_email(email, var1, var2):
    url = "https://api.msg91.com"

    payload = {
        "to":
        [
            {
                "name": f"{var1}",
                "email": f"{email}"
            }
        ],
        "from": {
            "name": "Alumni Portal",
            "email": "alumni.portal@pdxtnr.mailer91.com"
        },
        "domain": "pdxtnr.mailer91.com",
        "mail_type_id": "1",
        "template_id": "otp-login",
        "variables": {
            "VAR1": f"{var1}",
            "VAR2": f"{var2}"
        },
        "authkey": "377904AoGH8lt3b5GI629d3576P1"
    }

    headers = {
        'Content-Type': "application/JSON",
        'Accept': "application/json"
    }

    res = requests.post(url+"/api/v5/email/send",
                        json=payload, headers=headers)

    return res
