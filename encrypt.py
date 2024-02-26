from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import pandas as pd

salt = b'password1'

with open('salt.bin', 'wb') as f:
    f.write(salt)

password = "password2"

key = PBKDF2(password, salt, dkLen=32)

file = 'file.csv'
data = pd.read_csv(file)
print(data)

tobe = data.to_csv().encode()
print(tobe)

cipher = AES.new(key, AES.MODE_CBC)
file = cipher.encrypt(pad(tobe, AES.block_size))

print(file)

with open('file.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(file)
