from pwn import *
from subprocess import *
from ctypes import CDLL

libc = CDLL('libc.so.6')

def initSrand():
    return libc.srand(1)

HOST = "20.42.99.115"
PORT = 3143

r = remote(HOST, PORT)
initSrand()

value = libc.rand()
result = (value ^ 0xacedface)

print(result)
pause()
r.sendline(bytes(result))

r.interactive()