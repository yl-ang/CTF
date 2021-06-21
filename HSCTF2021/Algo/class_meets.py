from pwn import *

HOST = 'class-meets.hsc.tf'
    
PORT = 1337  
    
r = remote(HOST,PORT)


while True:
    try:
        print(r.recvuntil('!\n'))
        r.recvuntil('M')
    except:
        break

    # start mth/date
    m1 = int(r.recvuntil(' D', drop = True).decode('utf-8'))
    d1 = int(r.recvuntil('\n', drop = True).decode('utf-8'))

    r.recvuntil('M')

    # end mth/date
    m2 = int(r.recvuntil(' D', drop = True).decode('utf-8'))
    d2 = int(r.recvuntil('\n', drop = True).decode('utf-8'))

    r.recvuntil('I')

    # student 1's config
    s1_i = int(r.recvuntil(' V', drop = True).decode('utf-8'))
    s1_v = int(r.recvuntil('\n', drop = True).decode('utf-8'))

    r.recvuntil('I')

    # student 2's config
    s2_i = int(r.recvuntil(' V', drop = True).decode('utf-8'))
    s2_v = int(r.recvuntil('\n', drop = True).decode('utf-8'))

    print(m1,d1,m2,d2,s1_i,s1_v,s2_i,s2_v)

    # number of days
    days = 360

    # initialise number of days in mth
    mth_1 = [0]*days
    mth_2 = [0]*days

    # initialise rotations of student 1 and student 2
    student_1 = ('i'*s1_i + 'v'*s1_v)*days
    student_2 = ('i'*s2_i + 'v'*s2_v)*days

    count = 0
    match = 0

    # count number of matches
    for d in range(0,len(mth_1)):
        if d%7 == 5 or d%7 == 6:
            mth_1[d] = 'w'
            mth_2[d] = 'w'
            continue
        else:
            mth_1[d] = student_1[count]
            mth_2[d] = student_2[count]
            count += 1
        if (d >= m1*30+d1 and d <= m2*30+d2) and (mth_1[d] == mth_2[d]):
            match += 1

    r.sendline(str(match))
    
print(r.recvall())

# flag = flag{truly_4_m45t3r_4t_c00rd1n4t1n9_5ch3dul35}