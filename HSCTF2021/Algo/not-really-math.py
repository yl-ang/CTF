from pwn import *

HOST = 'not-really-math.hsc.tf'
PORT = 1337

r = remote(HOST,PORT)

r.recvuntil('=\n')

while True:
    try:
        question = r.recvuntil(':', drop = True).decode('utf-8')
    except:
        break


    x = []

    add = 0
    digits = ''

    for i in question:
        if i.isdigit():
            digits += i
        elif i == 'a':
            x.append(int(digits))
            x.append('a')
            digits = ''
        elif i == 'm':
            x.append(int(digits))
            x.append('m')
            digits = ''
        else:
            x.append(int(digits))
            

    y = []

    for i in range(0,len(x)):
        if str(x[i]).isdigit():
            if add == 1:
                digit = y[-1]
                y.pop()
                y.append(digit + x[i])
                add = 0
            else:
                y.append(x[i])
        elif x[i] == 'a':
            add = 1
        else:
            continue


    z = 1        

    if len(y) == 1:
        r.sendline(str(y[0]%(pow(2,32)-1)))
    else:
        for j in range(0,len(y)):
            z *= y[j]
        r.sendline(str(z%(pow(2,32)-1)))
        z = 1

    r.recv()

print(r.recvall())

# flag = flag{yknow_wh4t_3ls3_is_n0t_real1y_math?_c00l_m4th_games.com}
