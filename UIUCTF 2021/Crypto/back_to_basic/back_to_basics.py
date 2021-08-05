from Crypto.Util.number import long_to_bytes, bytes_to_long
from gmpy2 import mpz, to_binary

with open("flag_enc_base", "rb") as f:
    content = f.read()

ALPHABET = bytearray(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#")

def base_n_decode(bytes_in, base):
    bytes_out = to_binary(mpz(bytes_in, base=base))[:1:-1]
    return bytes_out

while "uiuctf" not in str(content):
    # print(content)
    for i in range(2,37):
        try:
            result = base_n_decode(content,i)
            print(result)
            if "\\" not in str(result):
                content = result
                print("%s is the key char" % i)
        except:
            pass