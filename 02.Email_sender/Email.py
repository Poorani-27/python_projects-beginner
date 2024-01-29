
# Import necessary modules
from email.message import EmailMessage
from app import password # Import the 'password' variable from the 'app' module
import ssl
import smtplib

# Set up email details
Email_sender = "tpoorani2002@gmail.com"
Email_password = password #enter your password
Email_receiver = input("\n\tEnter A Valid Email Id to Send Message : ")
subject = input("\tEnter The Subject : ")
body = input("\tEnter Your Message  here:\n\t\t")
# Create an EmailMessage object
em =EmailMessage()
em['From '] :Email_sender
em ['To'] = Email_receiver
em['subject']=subject
em.set_content(body)
# Set up SSL context for secure connection
context = ssl.create_default_context()
with smtplib.SMTP_SSL('SMTP.gmail.com',465,context=context) as smtp:
     # Login to the email account
    smtp.login(Email_sender,Email_password)
    # Send the email
    smtp.sendmail(Email_sender,Email_receiver, em.as_string())