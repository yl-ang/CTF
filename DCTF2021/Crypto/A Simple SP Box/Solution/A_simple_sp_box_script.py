from pwn import *
from subprocess import *
from math import ceil, log

# possible ascii characters in the flag
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!@#$%.'\"+:;<=}{"

# remote connection to host server
HOST = "dctf1-chall-sp-box.westeurope.azurecontainer.io"
PORT = 8888

r = remote(HOST, PORT)

r.recvuntil('\n')

#retrieving encrypted flag from server
encrypted = r.recvuntil('\n', drop = True).decode('utf-8')

# loop to find each possible characters' encryption
for i in ALPHABET:
    payload = ''
    payload += i*42
    r.sendline(payload)
    r.recvuntil('\n')
    value = r.recvuntil('\n', drop = True)
    value = value.decode('utf-8')[0]
    newlist.append(value)
    r.recv()

# mapping encrypted character with itself
S_box = {k : v for k, v in zip(newlist, ALPHABET)} 

# decrypting the flag
flag = [S_box[c] for c in encrypted]

# now to rearrange the position of the decrypted flag
rounds = int(2 * ceil(log(len(encrypted), 2))) # given in src code

encrypted = flag
newlist = []

# rearranging the flag to its original position
for num in range(rounds-1):
    new_enc = []
    even = int(len(encrypted)/2)
    odd = 0
    for index in range(int(len(encrypted)/2)):
        new_enc.append(encrypted[even])
        new_enc.append(encrypted[odd])
        even += 1
        odd += 1
    encrypted = new_enc

flag = ''.join(encrypted)

# sending flag into the server
r.sendline(flag)

print(r.recv())