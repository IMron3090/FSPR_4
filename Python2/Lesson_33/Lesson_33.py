import os
import smtplib, ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = "programmist924@gmail.com"
message["To"] = "eltnpubgmobile@gmail.com"

sender_email = "programmist924@gmail.com"
password = "omgurqnjwfjgbkxp"
receiver_email = "eltnpubgmobile@gmail.com"
text = """/
hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python fourth time</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""


part1 = MIMEText(text,"plain")
part2 = MIMEText(text,"html")


message.attach(part1)
message.attach(part2)
# context = ssl.create_default_context()
print("sending email...")
with smtplib.SMTP("localhost",1025)as server:
    # server.login(sender_email,password)
    server.sendmail(
    sender_email,receiver_email,message.as_string()
)
    print("Email was sent!")
