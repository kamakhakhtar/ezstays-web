from django.core.mail import send_mail
from django.conf import settings

def send_email_to_client(message):
    subject = "This email from django server"
    # message ="This is test message"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["kamakh.akhtar@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)