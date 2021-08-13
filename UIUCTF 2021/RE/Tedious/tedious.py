import gdb

ALPHABET = "{abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!@#$%.'\"+:;<=}{?"
FINAL = [0x4d,0xb9,0x4d,0xb,0xd4,0x66,0xe3,0x29,0xb8,0x4d,0xdf,0x66,0xb8,0x4d,0xe,0xc4,0xdf,0xd4,0x14,0x3b,0xdf,0x66,0x2c,0x14,0x47,0xdf,0xb7,0xb8,0xb7,0xdf,0x47,0x4d,0xa4,0xdf,0x32,0xb8,0xea,0xf5,0x92]

   
# bp at CMP
gdb.execute('b *0x8001999')

flag = 'uiuctf{y0u_f0unD_t43_fl4g_w0w_gud_j0b}'

counter = 38

for _ in range(0x27-37):
    for i in ALPHABET:
        flag += i
        orig_len = len(flag)
        gdb.execute('run < ' + "<(python -c 'print(\"" + ''.join(flag) + "\")')")
                                
        for count in range(0x27):
            if count == counter:
                
                gdb.execute('p $rax')
                eax = gdb.parse_and_eval("$rax")
                                
                gdb.execute('p $rdx')
                edx = gdb.parse_and_eval("$rdx")
                
                if edx != eax:
                    flag = flag[:-1]
                else:
                    counter += 1
                break
            
            gdb.execute('c')

        if len(flag) != orig_len:
            continue
        else:
            with open('flag_uiuctf.txt', 'w') as f:
                f.write(flag)
            break
        
