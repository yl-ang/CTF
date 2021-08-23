import string

primes_less_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

final = "ujp?_oHy_lxiu_zx_uve"
prime_rot_values = []
for i in range(20):
    # print("local_fc is %s" % ())
    temp = i << 2
    for j in primes_less_100:
        if temp < j:
            prime_rot_values.append(j)
            break
print(prime_rot_values)

def make_rot_n(n):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = str.maketrans(lc + uc,
                          lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: str.translate(s, trans)

flag = "corctf{"
count = 0
for k in prime_rot_values:
    flag += make_rot_n((26 - k) % 26)(final[count])
    print(flag)
    count += 1
flag += "}"
print(flag)