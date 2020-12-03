import smtplib
from feedbackform.static_config_parser import StaticConfigParser

config = StaticConfigParser()
EMAIL_ADDRESS = config.get('EMAIL', 'email_address')
EMAIL_PASSWORD = config.get('EMAIL', 'email_password')

class SendEmail():
    def __init__(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo() # identify ourselves with gmail
            smtp.starttls() # encrypt traffic
            smtp.ehlo() # re-identify ourselves as encrypted traffic

            print(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = "hello there"
            body = "epic body paragraph"

            message = f"Subject: {subject}\n\n{body}"

            smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message) # email ourselves
    
    def send(self, subject, body):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo() # identify ourselves with gmail
            smtp.starttls() # encrypt traffic
            smtp.ehlo() # re-identify ourselves as encrypted traffic

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            message = f"Subject: {subject}\n\n{body}"

            smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message) # email ourselves