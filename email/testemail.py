#!/usr/bin/env python3
import sys, os
import smtplib
from email.message import EmailMessage

with open('mail_contents.txt', 'r') as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())

msg['Subject'] = 'The contents of mail_contents.txt'
msg['From'] = 'dwc62@drexel.edu'
msg['Reply-To'] = 'david.chin.work@gmail.com'
msg['To'] = 'david.chin@drexel.edu'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()


