def cold(string):
    return string[16:] + string[0:16]

def cool(string):
    s = ''
    for i in range(0,len(string)):
        if i%2 == 0:
            s += chr(ord(string[i])-3*(i//2))
        else:
            s += string[i]
    return s
def warm(string, index):
    index_3 = string.find('3')
    a = string[string.index('3',index_3+1):]
    sec_half = string[0:string.index('3',index_3+1)] 
    b = string[index:string.index('3',index_3+1)]
    c = string[0:index]
    return a + b + c
    
def hot(string):
    int_list = [-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, -73, 40, -27,
                -73, -13, 0, 0, -68, 10, 45, 13]
    s = ''
    for i in range(0,len(string)):
        s += chr(ord(string[i])-int_list[i])
    return s

string = '4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy'

for i in range(0,len(string)):
    try:
        flag = cold(cool(warm(hot(string),i)))
    except:
        continue
    if 'flag' in flag:
        print(flag)
   
# flag = flag{1ncr34s3_1n_3nth4lpy_0f_5y5}