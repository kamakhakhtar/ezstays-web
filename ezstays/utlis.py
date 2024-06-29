from pymongo import MongoClient
from django.core.mail import send_mail
from django.conf import settings
import datetime  # Import the datetime module

def send_email_to_client(message):
    # Split the message into lines and extract the first line
    first_line = message.split('\n')[0]
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    subject = "Ezstays " + first_line + "Query at : " + current_datetime
    
    # Log the email in the database
    
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["info@ezstays.in", "kamakh.akhtar@gmail.com", "dmarketingonline2014@gmail.com"]
    bcc_list = ["kamakh.akhtar@gmail.com", "dmarketingonline2014@gmail.com"]
    
    # MongoDB connection settings
    client = MongoClient("mongodb://arshad:arshad7312@184.164.142.211:27017/tatkalworld?tls=false&authSource=admin")
    db = client["Ezstays"]
    collection = db["mail"]

    # Insert the email log into MongoDB
    email_log = {
        "subject": subject,
        "message": message,
        "recipient": "; ".join(recipient_list),
        "sent_datetime": datetime.datetime.now()
    }

    collection.insert_one(email_log)

    # Send the email with BCC recipients
    send_mail(
        subject,
        message,
        from_email,
        recipient_list
    )


# Ensure you have the correct MongoDB settings
