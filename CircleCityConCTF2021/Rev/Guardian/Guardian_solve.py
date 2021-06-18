from pwn import *
from subprocess import *

HOST = "35.224.135.84"
PORT = "2000"

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!@#$%.'\"+:;<=}{?"
flag = "CCC{let_m3_thr0ugh!_let_me_p4ss!_d0_y0u_th1nk_y0u_c4n_h3lp_h3r?}"

def brute(char): 
    r = remote(HOST, PORT)
    r.recvuntil('d?\n>')
    r.sendline(char)
    try:
        line = r.recvuntil('\nH', drop = True)
    except:
        return r.recvall()
    return line

while True:
    for char in ALPHABET:
        line = brute(flag+char)
        print(line)
        count = line.split()
        if len(count) == len(flag)+1:
            flag += char
            break
    if '}' in flag: # alr have a check in place such that length == 64, program will break and exit
        print(flag)
        break
    print(flag)
    
