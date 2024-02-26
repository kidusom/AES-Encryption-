from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

salt = b'password1'
password = "password2"

key = PBKDF2(password, salt, dkLen=32)

with open('file.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)

b = original.decode('utf-8')
print(b)

with open('file.csv', 'wb') as f:
    f.write(b.encode())
