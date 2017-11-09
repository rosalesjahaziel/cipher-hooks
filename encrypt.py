import os
from Crypto.Cipher import AES

KEY = os.environ['cryptkey']
iv = 16 * b"\x00"

def encrypt_file():
    cipher = AES.new(KEY, AES.MODE_CFB, iv)
    plain_file = open("data.py","r")
    secure_file = open("temp_data.py","w")
    crypt_value = iv + cipher.encrypt(plain_file.read())
    secure_file.write(crypt_value)    
    secure_file.close()
        
if __name__ == '__main__':
    exit(encrypt_file())