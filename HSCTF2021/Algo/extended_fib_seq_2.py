def fibo2(n):
    out = [4, 5]
    for i in range(n+1): 
        out.append(out[-1]+out[-2])
        if i != 0:
             out[i] = out[i-1]+out[i]
    return out


from pwn import *

HOST = 'extended-fibonacci-sequence-2.hsc.tf'
    
PORT = 1337  
    
r = remote(HOST,PORT)    

while True:
    try:
        r.recvuntil('!\n')
        n = int(r.recvuntil('\n',drop = True).decode('utf-8'))
    except:
        break
    
    r.sendline(str(sum(fibo2(n)[:-2]))[-10:].lstrip('0'))
    
    r.recv()

print(r.recvall())

# flag = flag{i_n33d_a_fl4g._s0m3b0dy_pl3ase_giv3_m3_4_fl4g.}