from django.core.mail import send_mail
from django.conf import settings
from myapp.models import SentEmail  # make sure to import the SentEmail model


def send_email_to_client(message):
    # Split the message into lines and extract the first line
    first_line = message.split('\n')[0]
    subject = "Email from ezstays website : " + first_line
    # Log the email in the database
    print(subject)
    # message ="This is test message"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["info@ezstays.in","kamakh.akhtar@gmail.com", "mrpratap51@gmail.com "]
    # Define BCC recipient(s)
    bcc_list = ["kamakh.akhtar@gmail.com", "mrpratap51@gmail.com "]  # Add the BCC addresses here
     # Send the email with BCC recipients
    send_mail(
        subject,
        message,
        from_email,
        recipient_list
    )


    SentEmail.objects.create(
        subject=subject,
        message=message,
        recipient="; ".join(recipient_list)  # Joining the list to store as a string
    )