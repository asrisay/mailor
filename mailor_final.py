import smtplib

gmail_user = input("Please enter your email address:\n ")
gmail_password = input("Please enter your password below:\n ")


sent_from = gmail_user
to = input("Please enter email address to send to: \n ")
subject = input("Please enter email subject: \n ")
body = input("Please enter the body of email: \n ")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Email failed to sent!",ex)