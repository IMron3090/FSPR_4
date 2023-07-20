# import smtplib
# import os

# def send_email(message):
#     sender = "programmist924@gmail.com"
#     password = os.getenv("Email Password")

#     server = smtplib.SMTP("smtp.gmail.com",587)
#     server.starttls()

#     try:
#         server.login(sender,password)
#         server.sendmail(sender,sender,f"Subject:Call me please!\n{message}")

#         return "The message was sent successfully!"
#     except Exception as _ex:
#         return f"{_ex}\nCheck your login or password please!"
    
# def main():
#     message = input("Type your message:")
#     print(send_email(message=message))

# if __name__ == "__main__":
#     main()

# ==================================================
import smtplib


from_address = 'programmist924@gmail.com'
password = 'omgurqnjwfjgbkxp'


email_addresses = ['eltnpubgmobile@gmail.com',
                       'eltnpubgmobile@gmail.com']


email_text = """
Hello Imran,

How old are you

Regards,
Sender
"""


SMTP_server = smtplib.SMTP('localhost', 750)
SMTP_server.starttls()
SMTP_server.login(from_address, password)


for to_address in email_addresses:
    SMTP_server.sendmail(from_address, to_address, email_text)


SMTP_server.quit()
