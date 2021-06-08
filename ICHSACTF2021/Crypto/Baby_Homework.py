# AES ECB -- One byte at a time attack

from pwn import *

def main(data):
    host = 'baby_homework.ichsa.ctf.today'
    port = 8010
    t = remote(host, port)
    t.sendline(data)
    t.recvuntil("Hello! What do you want to encrypt today?\n")
    a = t.recvline()[36:38]
    return a

if __name__ == '__main__':
    
    # restored flags
    flag  ="d0n7_7ruzt_DeF4uL7_V4lu3z"
    flag1 ="d0n7_7ruzt_DeF4u"
    flag2 ="L7_V4lu3z"
    count = 13
    while True:
        for i in range(33,125):
            print(i)
            input1 = "A" * count
            a = main(input1)
            input2 =  "A" * count + flag1 + flag2 + chr(i)
            b = main(input2)
            if a == b:
                print("yes flag is %s " % chr(i))
                flag2 = flag2 + chr(i)
                print(flag2)
                count = count - 1
                break
        if count == -1:
            print("restored flag %s" % (flag1 + flag2))
            break