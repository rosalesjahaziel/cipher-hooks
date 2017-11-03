import os
import random
import struct
from Crypto.Cipher import AES

KEY = os.environ['cryptkey']
iv = 16 * b"\x00"

class encryption_files:

    def crypt_value(self, file_name):
        cipher = self.generete_new_AES_obj()
        plain_file = open(file_name,"r")
        secure_file = open("temp_data.py","w")
        crypt_value = iv + cipher.encrypt(plain_file.read())
        print crypt_value
        secure_file.write(crypt_value)    
        secure_file.close()
        
    def decrypt_value(self, file_name):
        cipher = self.generete_new_AES_obj()
        crypt_value = open(file_name,"r")
        plain_file = open("data.py","w")
        decrypt_value = cipher.decrypt(crypt_value.read())
        print decrypt_value[16:]
        plain_file.write(decrypt_value[16:]) 
        plain_file.close()

    def generete_new_AES_obj(self):
        cipher = AES.new(KEY, AES.MODE_CFB, iv)
        return cipher

class encryption_text:

    def crypt_value(self, msg):
        cipher = self.generete_new_AES_obj()
        crypt_value = iv + cipher.encrypt(msg)
        print crypt_value
        return crypt_value

    def decrypt_value(self, msg):
        cipher = self.generete_new_AES_obj()
        decrypt_value = cipher.decrypt(msg)
        print decrypt_value[16:]
        return decrypt_value[16:]

    def generete_new_AES_obj(self):
        cipher = AES.new(KEY, AES.MODE_CFB, iv)
        return cipher
