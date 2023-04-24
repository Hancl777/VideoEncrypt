import numpy as np
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
import binascii

# SM4
# value = b'111' #  bytes类型
# crypt_sm4 = CryptSM4()
# crypt_sm4.set_key(key, SM4_ENCRYPT)
# encrypt_value = crypt_sm4.crypt_ecb(value) #  bytes
# crypt_sm4.set_key(key, SM4_DECRYPT)
# decrypt_value = crypt_sm4.crypt_ecb(encrypt_value) #  bytes
# assert value == decrypt_value


key = b'3l5butlj26hvv313'
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'


class enc:

    def __init__(self, key):
        """
        :param key: 密钥 string
        """
        # 实例化并初始化
        self.crypt_sm4 = CryptSM4()
        self.crypt_sm4.set_key(key, SM4_ENCRYPT)

    @classmethod
    def encrypt_ecb(self, value):
        """
        :param value: bytes
        :return: bytes
        """
        # 返回值为bytes
        encrypt_value = self.crypt_sm4.crypt_ecb(value)
        return encrypt_value

    @classmethod
    def encrypt_cbc(self, value, iv):
        """
        :param value: bytes
        :return: bytes
        """
        encrypt_value = self.crypt_sm4.crypt_cbc(iv, value)
        return encrypt_value

    @classmethod
    def str_to_hexStr(self, hex_str):
        """
        :param hex_str: 字符串
        :return: hex
        """
        hex_data = hex_str.encode('utf-8')
        str_bin = binascii.unhexlify(hex_data)
        return str_bin.decode('utf-8')
