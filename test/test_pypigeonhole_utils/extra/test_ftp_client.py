import unittest
from unittest import mock

import pypigeonhole_utils.simple.network_utils as net_utils
import pypigeonhole_utils.extra.ftp_client as ftp_client


# another way to test is to use a stub server: https://github.com/rspivak/sftpserver
# https://medium.com/python-pandemonium/python-mocking-you-are-a-tricksy-beast-6c4a1f8d19b2
class FtpClientTest(unittest.TestCase):
    def setUp(self):
        self.ftp_client = ftp_client.FtpClient(
            net_utils.RemoteServer('ftp_server', 22),
            net_utils.Credential(user='userId', ssh_key_file='somekey.ppk'),
            net_utils.ProxyServer('proxy_server', 8080, net_utils.ProxyType.SOCKS4)
        )

    @mock.patch("paramiko.SSHClient")
    @mock.patch("paramiko.SFTPClient")
    def test_sftp(self, mock_ssh_client, mock_sftp_client):
        # mock_sftp_client.from_transport.return_value = mock_sftp_client

        missing = self.ftp_client.download(['some file'], '/tmp/download')
        self.assertTrue(len(missing) == 0)

        # we see error: cryptography.hazmat.binding._openssl ImportError: DLL load failed
        # pip install --upgrade --force paramiko

    @mock.patch("paramiko.SSHClient", autospec=True)
    @mock.patch("paramiko.SFTPClient", autospec=True)
    def test_file_not_found(self, mock_ftp_client, mock_ssh_client):
        mock_sftp = mock.MagicMock()
        mock_sftp.get.side_effect = FileNotFoundError('file missing', 'test')
        mock_sftp.my_marker = 123

        mock_ftp_client.from_transport.return_value.__enter__.return_value = mock_sftp

        missing = self.ftp_client.download(['not_found.file'], '/tmp/download')
        self.assertTrue(len(missing) == 1)
