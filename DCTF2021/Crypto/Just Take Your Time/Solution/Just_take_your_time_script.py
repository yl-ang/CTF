from pwn import *
from subprocess import *
import math
from Crypto.Cipher import DES3
from time import time
from random import randint
from secrets import token_hex


HOST = "dctf-chall-just-take-your-time.westeurope.azurecontainer.io"
PORT = "9999"
 
r = remote(HOST, PORT)

r.recvuntil('\n')
a = r.recvuntil(' *', drop = True)
r.recvuntil(' ')
b = r.recvuntil(' =', drop = True)

product = int(a) * int(b)

r.sendline(str(product))

print(r.recv())
print(r.recvuntil('\n'))
secret = r.recvuntil('\n', drop = True)

key = str(int(time())).zfill(16).encode("utf-8")
dicipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
decrypted = dicipher.decrypt(bytes.fromhex(secret.decode('utf-8')))

try:
    for i in range(0,3):
        r.sendline(decrypted)
except: 
    pass

print(r.recvall())