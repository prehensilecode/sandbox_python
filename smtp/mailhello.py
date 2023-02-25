#!/usr/bin/env python3
import sys
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import smtplib

msg = MIMEMultipart()
msg['From'] = 'foobar@example.com'
msg['To'] = 'barfoo@example.com'
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = 'Hello world'

message_body = 'hello, world - run by normal user'

msg.attach(MIMEText(message_body))

with smtplib.SMTP('some_smtp_server') as mailserver:
    mailserver.send_message(msg)

