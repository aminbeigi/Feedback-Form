import smtplib
from feedbackform.static_config_parser import StaticConfigParser

config = StaticConfigParser()
EMAIL_ADDRESS = config.get('EMAIL', 'email_address')
EMAIL_PASSWORD = config.get('EMAIL', 'email_password')

class SendEmail():
    def send(self, subject, body):
        # quits automatically
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo() # identify ourselves with gmail
            smtp.starttls() # put SMTP connection in TLS mode
            smtp.ehlo() # re-identify ourselves as encrypted traffic
            
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            message = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message) # email ourselves