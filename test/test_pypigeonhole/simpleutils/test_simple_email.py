import unittest
import unittest.mock as mock

import pypigenhole.simpleutils.network_utils as net_utils
import pypigenhole.simpleutils.simple_email as simple_email


class SimpleEmailTest(unittest.TestCase):
    @mock.patch.object(simple_email.EmailServer, 'send_text', return_value={})
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
            res = email_server.send_text(text, envelop)
            print(res)
            self.assertTrue(len(res) == 0)  # no error
