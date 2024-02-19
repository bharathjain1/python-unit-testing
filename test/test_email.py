import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
import unittest
from unittest.mock import Mock,patch,ANY

def send_email(smtp_server,smtp_port,from_addr,to_addr,subject,body):
    msg = MIMEMultipart()
    msg['from'] = from_addr
    msg['to'] = to_addr
    msg['subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(from_addr,"password")
    text = msg.as_string()
    server.sendmail(from_addr,to_addr,text)
    server.quit()

class TestEmail(unittest.TestCase):
    
    @patch('smtplib.SMTP')
    def test_send_email(self,mock_smtp):
        isinstance = mock_smtp.return_value

        send_email("smtp@example.com",123,"me@example.com","his@email.com","cars","cars content")

        isinstance.starttls.assert_called_with()
        isinstance.login.assert_called_with("me@example.com","password")
        isinstance.sendmail.assert_called_with("me@example.com","his@email.com",ANY)
        isinstance.quit.assert_called_with()



if __name__ == "__main__":
    unittest.main()


