/*
Challenge Description: 

One of our field agents stole a program that the GDC used to encrypt data and an encrypted file. 
Help us to decrypt the file. All we know is that it is encrypted using XOR and that the length of the key is 6. 
We also know the original message contains the word “Never”.
*/

while (local_14 < local_24) {
putc((uint)*(byte *)((long)local_418 + (long)local_14) ^
        (int)*(char *)((long)local_c + *(long *)(param_2 + 0x10)),local_20);
local_c = local_c + 1;
if (local_c == local_18) {
    local_c = 0;
}
local_14 = local_14 + 1;
}

/*
From the hint and the pseudo c code, we are able to see that the flag is xor-ed with the key of length 6 in a loop
and written into the enc_data. So we need to reverse the xoring.

We tried https://www.dcode.fr/xor-cipher and use the key size of 6.

key in hex: 313131393730
flag: CDDC21{It_@ll_$tarted_Th3n}
*/

