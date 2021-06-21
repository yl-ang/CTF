def decrypt(message, key):
    random.seed(key)
    l = list(range(len(message)))
    random.shuffle(l)
    return [message[i] for i, x in sorted(enumerate(l), key=lambda x: x[1])]


flag = list('QQ.ap(OOOaQa.a($/FF.F/ZOZ..aQaQ/aa(a(ZZaaF.Q^FaZ,S/..(^]aF.FF.pFF-(==SFa/aOo.=/aFM/,.,Z=/aF/aQ/*<Q(^-OSZOO=a]Q](Q<].a~/ao/aYZaF=aQa]Q^FOZFsQn/^FOh.*aZ.OaaO/(Q.SZ</ QQ,a(OFaFF((QQQaQQ/^/Q.O-F(Z(=gQQ=k,OSF=F.a/]Q=Z(Qa(ao=a:ZQ/QpJ]/QQF.=FZ]QkFS^=Q:QQZQFa=."OS(=^Q.^Ja/(/Z^]F:]//./.Q=F=Ya/SO/]Oas=apS=(..)(.aF/(oZ(a/~.,,ZZZ/Oq=(.QF":.|O($FZ./(]]FO]FO.Oo"F+QO/FqY/Z-(a.=/F/aa/.=OZOFQ(=Z./pOa((O]..Q/]Q((a(]/aaSZJ.Q(*F]<//Fa/|]QFQZ(=S.ZQQZOFQa:Q/aQO=(]..a/^(QOQoF////(^kF-a-')

for i in range(0, len(flag), 2):
    flag[i], flag[i + 1] = flag[(i + 1)], flag[i]

x = ['t', 'Y', 'w', 'V', '|', ']', 'u', 'X', '_', '0', 'P', 'k', 'h', 'D', 'A', '4', 'K', '5', 'z',
 'Z', 'G', '7', ';', 'S', ' ', '/', '6', '%', '}', '\\', ',', ':', '>', '#', 'a', '$', '3', '`',
 '+', 'R', 'b', 'H', 'd', 's', '1', 'J', 'L', 'v', '9', '2', 'o', 'M', '<', 'e', '(', 'x', '-',
 'B', 'm', "'", 'y', 'Q', '"', 'W', 'l', '.', 'i', 'O', '^', 'p', '8', 'f', 'F', 'C', '?', 'g',
 '@', 'j', '[', 'r', '!', '=', 'E', '~', '*', 'T', '{', ')', 'U', 'N', 'c', '&', 'n', 'q', 'I']

seed = 1618514508 # coverted from CAT timezone to epoch (pyc decompiler uses CAT timezone)


flag = decrypt(''.join(flag),seed)

for _ in range(20):
    for i in range(len(flag)):
        flag[i] = chr((x).index(flag[i]) + 32)

final = ''.join(flag)

print(final)
        
# flag = flag{71me5t4mp_fun}

# epoch time converter: http://tools.up2a.info/en/epochtimes