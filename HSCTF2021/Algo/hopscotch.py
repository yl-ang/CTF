# Algo adapted from :https://www.geeksforgeeks.org/ways-sum-n-using-array-elements-repetition-allowed/

def solve(arr, m, N):
 
    count = [0 for i in range(N + 1)]
     
    # base case
    count[0] = 1
     
    # Count ways for all values up
    # to 'N' and store the result
    for i in range(1, N + 1):
        for j in range(m):
 
            # if i >= arr[j] then
            # accumulate count for value 'i' as
            # ways to form value 'i-arr[j]'
            if (i >= arr[j]):
                count[i] += count[i - arr[j]]
     
    # required number of ways
    return count[N]
     
from pwn import *

HOST = 'hopscotch.hsc.tf'
    
PORT = 1337  
    
r = remote(HOST,PORT)

r.recvuntil('=\n')

while True:
    try:
        n = int(r.recvuntil('\n:',drop=True).decode('utf-8'))
    except:
        break
    
    arr = [1, 2]
    m = len(arr)
    r.sendline(str(solve(arr,m,n)%10000))

    r.recv()

print(r.recvall())

# flag = flag{wh4t_d0_y0U_w4nt_th3_fla5_t0_b3?_'wHaTeVeR_yOu_wAnT'}