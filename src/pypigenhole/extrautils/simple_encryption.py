import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


# modified from: https://stackoverflow.com/questions/42568262/how-to-encrypt-text-with-a-password-in-python
# do not pretend to be a security expert, leave it to pro.

# the 2 methods here are universal for all crypto, differences should be in constructors.
# RSA based or other approaches should be in separate files to avoid unnecessary lib dependencies
class CryptoAES:
    def __init__(self, key: str, base64_encoding='latin-1'):
        self._key = key.encode('utf-8')
        # if this is None, it means no encoding. use ascii, latin-1, or others
        self._base64_encoding = base64_encoding

    def encrypt_secret(self, message: str):
        key = SHA256.new(self._key).digest()  # use SHA-256 over our key to get a proper-sized AES key
        iv = Random.new().read(AES.block_size)  # generate IV
        encryptor = AES.new(key, AES.MODE_CBC, iv)

        secret_bytes = message.encode('utf-8')
        padding = AES.block_size - len(secret_bytes) % AES.block_size  # calculate needed padding
        secret_bytes += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
        data = iv + encryptor.encrypt(secret_bytes)  # store the IV at the beginning and encrypt
        return base64.b64encode(data).decode(self._base64_encoding) if self._base64_encoding else data

    def decrypt_secret(self, message):
        if self._base64_encoding:
            message = base64.b64decode(message.encode(self._base64_encoding))
        key = SHA256.new(self._key).digest()  # use SHA-256 over our key to get a proper-sized AES key
        iv = message[:AES.block_size]  # extract the IV from the beginning
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        data = decryptor.decrypt(message[AES.block_size:])  # decrypt
        padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
        if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
            raise ValueError("Invalid padding encoded..." + message)

        ret = data[:-padding]  # remove the padding
        return ret.decode('utf-8')
