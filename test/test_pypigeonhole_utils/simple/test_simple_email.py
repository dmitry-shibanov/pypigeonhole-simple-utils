import unittest
import unittest.mock as mock

import pypigeonhole_utils.simple.network_utils as net_utils
import pypigeonhole_utils.simple.simple_email as simple_email
import smtplib


class SimpleEmailTest(unittest.TestCase):
    # rewrite this: mock _smtp_sender
    @mock.patch.object(smtplib.SMTP_SSL, 'send_message', return_value={})
    @mock.patch.object(simple_email.EmailServer, '__enter__')
    @mock.patch.object(simple_email.EmailServer, '__exit__')
    def test_port_465(self, mock1, mock2, mock3):
        text = 'This is a test message'
        subject = 'Python email test'

        email_server = simple_email.EmailServer(
            net_utils.RemoteServer('smtp.some.com', 465),
            net_utils.Credential('sender@some.com', '')
        )
        with email_server:
            envelop = simple_email.Envelop(subject, 'sender@some.com', 'receiver@another.com')
            email_server._smtp_sender = mock1
            res = email_server.send_text(text, envelop)
            print(f'result: {res}')
            self.assertTrue(len(res) == 0)  # no error
