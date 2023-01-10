import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

print("deployment completed")
webbrowser.open("http://google.com")


########## send email ################

message = MIMEMultipart()
message["from"] = "Qiguo Sun"
message["to"] = "2359181042@qq.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=57) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sunqiguo1992@gmail.com", "ssssssasdasdasda")
    smtp.send_message(message)
    print("sent......")
