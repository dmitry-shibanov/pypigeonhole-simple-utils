from dataclasses import dataclass
import smtplib
from email.message import Message, EmailMessage

import pypigenhole.simpleutils.network_utils as network_utils


@dataclass
class Envelop:  # = namedtuple('Envelop', ['subject', 'from_addr', 'to_addr', 'headers'])
    subject: str
    from_addr: str
    to_addr: str
    headers: dict = None


class EmailServer:
    def __init__(self, email_server: network_utils.RemoteServer, credential: network_utils.Credential = None):
        self._email_server = email_server
        self._credential = credential
        self._smtp_sender = None

    def __enter__(self):
        if self._email_server.port == 465:
            self._smtp_sender = smtplib.SMTP_SSL(self._email_server.to_url())

            if self._credential:
                self._smtp_sender.login(self._credential.user, self._credential.password)
        else:  # 25 or 587
            self._smtp_sender = smtplib.SMTP(self._email_server.to_url())

            if self._credential:
                self._smtp_sender.login(self._credential.user, self._credential.password)
            else:
                self._smtp_sender.starttls()

        return self._smtp_sender

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._smtp_sender.quit()

    def send_text(self, text, envelop: Envelop):
        msg = Message()
        msg.set_payload(text)
        msg.add_header('Content-Type', 'text/html')
        return self.send(msg, envelop)

    def send_html(self, html, envelop: Envelop, alt_text=None):
        msg = EmailMessage()
        msg.set_payload(html)
        msg.add_header('Content-Type', 'text/html')
        if alt_text:
            msg.add_alternative(alt_text, 'plain')

        return self.send(msg, envelop)

    def send(self, message: Message, envelop: Envelop):
        message['Subject'] = envelop.subject
        message['From'] = envelop.from_addr
        message['To'] = envelop.to_addr

        if envelop.headers:
            for k, v in envelop.headers.items():
                if k in message:
                    message.replace_header(k, v)
                else:
                    message.add_header(k, v)

        return self._smtp_sender.send_message(message)
