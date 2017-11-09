import os
from Crypto.Cipher import AES

KEY = os.environ['cryptkey']
iv = 16 * b"\x00"
       
def decrypt_file():
    cipher = AES.new(KEY, AES.MODE_CFB, iv)
    crypt_value = open("temp_data.py","r")
    plain_file = open("data.py","w")
    decrypt_value = cipher.decrypt(crypt_value.read())
    plain_file.write(decrypt_value[16:]) 
    plain_file.close()

if __name__ == '__main__':
    exit(decrypt_file())