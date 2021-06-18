from pwn import *
from subprocess import *
import math
from Crypto.Cipher import DES3
from time import time
from random import randint
from secrets import token_hex


HOST = "misc.bcactf.com"
PORT = "49156"

def func():
    r = remote(HOST, PORT)
    r.recvuntil('letter "')
    letter = r.recvuntil('"',drop=True).decode('utf-8')
    r.sendline(letter)

    while True:
        try:
            line = r.recvuntil(']]]')
        except:
            return r.recvall()
            break
        r.sendline(chr(13))
        
while True:
    result = func()
    print(result)
    if b'bca' in result:
        break
   