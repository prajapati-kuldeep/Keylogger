import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender, receiver, subject, body, smtp_config):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_config['server'], smtp_config['port'])
    server.starttls()
    server.login(smtp_config['username'], smtp_config['password'])

    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
