def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    x = f(n >> 1)
    y = f(n // 2 + 1)
    return g(x, y, not n & 1)


def e(b, j):
    return 5 * f(b) - 7 ** j


def d(v):
    return v << 1


def g(x, y, l):
    if l:
        return h(x, y)
    return x ** 2 + y ** 2


def h(x, y):
    return x * j(x, y)


def j(x, y):
    return 2 * y - x

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!@#$%.'\"+:;<=}{?"

output = "9273726921930789991758 166410277506205636620946 836211434898484229672 15005205362068960832084 226983740520068639569752018 4831629526120101632815236 203649875442 1845518257930330962016244 12649370320429973923353618 203569403526 435667762588547882430552 2189229958341597036774 175967536338 339384890916 319404344993454853352 -9165610218896 435667762522082586241848 3542248016531591176336 319401089522705178152 -22797257207834556 12649370160845441339659218 269256367990614644192076 -7819641564003064368 594251092837631751966918564"

list_op = [int(x) for x in output.split(' ')]

flag = ''

count = 0

for i in range(0,len(list_op)):
    for char in ALPHABET:
        inp = ord(char)
        if(d(e(inp,count))) == list_op[count]:
            flag += chr(inp)
            count += 1
            break
        
print(flag)

# flag = flag{s3qu3nc35_4nd_5um5}