
# Adapted fibo algo from: https://stackoverflow.com/questions/54883049/fibonacci-sequence-in-python-most-efficient

def fibo(n):
    out = [0, 1]
    for i in range(n+1): 
        out.append(out[-1]+out[-2])
        if i != 0:
            out[i] = (int(str(out[i-1])+str(out[i])))
    return out



from pwn import *

HOST = 'extended-fibonacci-sequence.hsc.tf'
    
PORT = 1337  
    
r = remote(HOST,PORT)    

r.recvuntil('=\n')

while True:
    try:
        n = int(r.recvuntil('\n:',drop = True).decode('utf-8'))
    except:
        break
    
    r.sendline(str(sum(fibo(n)[:-2]))[-11:].lstrip('0'))
    
    r.recv()

print(r.recvall())

# flag = flag{nacco_ordinary_fib}