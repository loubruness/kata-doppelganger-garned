import mail_sender
from user import User
from mail_sender import *


def test_send_v1():
    # TODO: write a test that fails due to the bug in MailSender.send_v1
    user = User(name="Lou", email="t.r@efrei.net")
    message = "Hello, Lou! You've got a new notification."

    mailSender = MailSender(HttpClient())
    mailSender.send_v1(user, message)
    
    assert mailSender.http_client.addresses == [user.email], "All addresses not addressed"


def test_send_v2():
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    user = User(name="Lou", email="t.r@efrei.net")
    message = "Hello, Lou! You've got a new notification."

    mailSender = MailSender(HttpClient())
    mail = mailSender.send_v2(user, message)
    
    assert mail.message == user.email, "Wrong recipient"

class HttpClient:
    def __init__(self):
        self.addresses = []
        self.step = 0
        
    def post(self, url, data):
        if self.step == 0:
            self.step += 1 
            return SendMailResponse(code=503, message="Unable to handle request")
        else:
            self.addresses.append(data.recipient)
            return SendMailRequest(code=200, message=data.recipient)
        
