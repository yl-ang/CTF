from pwn import *

p = remote("mc.ax" ,31796)

p.sendline(b'add flour')
p.sendline(b'add water')
p.sendline(b'add yeast')
p.sendline(b'add salt')
p.sendline(b'hide the bowl inside a box')
p.sendline(b'wait 3 hours')
p.sendline(b'work in the basement')
p.sendline(b'preheat the toaster oven')
p.sendline(b'set a timer on your phone')
p.sendline(b'watch the bread bake')
p.sendline(b'pull the tray out with a towel')
p.sendline(b'open the window')
p.sendline(b'unplug the fire alarm')
p.sendline(b'unplug the oven')

p.sendline(b'flush the bread down the toilet')
p.sendline(b'wash the sink')
p.sendline(b'clean the counters')
p.sendline(b'get ready to sleep')
p.sendline(b'close the window')
p.sendline(b'replace the fire alarm')
p.sendline(b'brush teeth and go to bed')
p.interactive()