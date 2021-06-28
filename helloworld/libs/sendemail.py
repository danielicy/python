from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
import smtplib

template = Template(Path("template.html").read_text())
body = template.substitute({"name": "John"})

message = MIMEMultipart()
message["from"] = "danielicy@hotmail.com"
message["to"] = "danielicwk@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("yoda.png").read_bytes()))

hotmailsmtp = "smtp-mail.outlook.com"
gmailsmtp = "smtp.gmail.com"

with smtplib.SMTP(host=hotmailsmtp, port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    #smtp.login("testuser@codewithmosh.com", "todayskyisblue1234")
    smtp.login("danielicy@hotmail.com", "N@nahN@hmanMeUm@n")
    smtp.send_message(message)

 #smtp.login("danielicy@hotmail.com", "N@nahN@hmanMeUm@n")
