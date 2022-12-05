import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "name_title.gmail.com"  # Give your email
    zigzag = "fylmnmiuejwgqhdc"  # Give your password
    receiver = "samikpandit02@gmail.com"  # Give the receiver's email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, zigzag)
        server.sendmail(username, receiver, message)
