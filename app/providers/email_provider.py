import requests
from app.config import MAILGUN_API_KEY, MAILGUN_DOMAIN

def send_email(to, subject, text):
    return requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"Excited User <mailgun@{MAILGUN_DOMAIN}>",
            "to": to,
            "subject": subject,
            "text": text
        }
    )