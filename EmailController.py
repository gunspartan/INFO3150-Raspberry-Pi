"""
Sending an Email with an Attachment using Python
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class EmailController:
    def __init__(self):
        self.SMTP_PORT = 587
        self.SMTP_SERVER = "smtp.gmail.com"
        self.EMAIL_SENDER = "info3150test@gmail.com"
        self.EMAIL_RECEIVER = "info3150authorizeduser@gmail.com"
        self.PSWD = "ouopevplygpbkhbf"
        self.SUBJECT = "UNRECOGNIZED FACE DETECTED"
        # Make the body of the email
        self.BODY = f"""
        Screenshot of unrecognized face here...
        """

    # Define the email function (dont call it email!)
    # def sendEmail(self, filename):
    #         # make a MIME object to define parts of the email
    #         msg = MIMEMultipart()
    #         msg['From'] = self.EMAIL_SENDER
    #         msg['To'] = self.EMAIL_RECEIVER
    #         msg['Subject'] = self.SUBJECT

    #         # Attach the body of the message
    #         msg.attach(MIMEText(self.BODY, 'plain'))

    #         # Open the file in python as a binary
    #         attachment= open(filename, 'rb')  # r for read and b for binary

    #         # Encode as base 64
    #         attachment_package = MIMEBase('application', 'octet-stream')
    #         attachment_package.set_payload((attachment).read())
    #         encoders.encode_base64(attachment_package)
    #         attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
    #         msg.attach(attachment_package)

    #         # Cast as string
    #         text = msg.as_string()

    #         # Connect with the server
    #         print("Connecting to server...")
    #         TIE_server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
    #         TIE_server.starttls()
    #         TIE_server.login(self.EMAIL_SENDER, self.PSWD)
    #         print("Successfully connected to server")
    #         print()

    #         # Send emails to "person" as list is iterated
    #         print(f"Sending email to: {self.EMAIL_RECEIVER}...")
    #         TIE_server.sendmail(self.EMAIL_SENDER, self.EMAIL_RECEIVER, text)
    #         print(f"Email sent to: {self.EMAIL_RECEIVER}")
    #         print()
    def sendEmail(self, subject, body):
        print(subject)
        print(body)