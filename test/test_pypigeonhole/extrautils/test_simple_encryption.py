import unittest

import pypigenhole.extrautils.simple_encryption as enc


class IocInjectTest(unittest.TestCase):
    def test_enc(self):
        key_str = 'secret_AES_key_string_to_encrypt/decrypt_with'
        secret = 'secret message to be encrypted'

        crypto = enc.CryptoAES(key_str)
        print('1st round:')
        encrypted = crypto.encrypt_secret(secret)
        print('enc = {}'.format(encrypted))
        decrypted = crypto.decrypt_secret(encrypted)
        print('dec = {}'.format(decrypted))
        self.assertTrue(decrypted == secret)

        print('2nd round: the encrypted message will be different every time.')
        encrypted1 = crypto.encrypt_secret(secret)
        print('enc = {}'.format(encrypted1))
        decrypted1 = crypto.decrypt_secret(encrypted1)
        print('dec = {}'.format(decrypted1))
        self.assertTrue(decrypted1 == secret)

        self.assertTrue(encrypted != encrypted1)
        # every run generates different encryption, but we can always recover same secret
