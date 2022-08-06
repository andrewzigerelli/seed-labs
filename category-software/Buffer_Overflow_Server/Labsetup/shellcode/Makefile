
all: 
	gcc -z execstack -o a64.out call_shellcode.c
	#gcc -m32 -z execstack -o a32.out call_shellcode.c

asm:
	objdump -D -Mintel,x86-64 -b binary -m i386:x86-64 codefile_64 > codefile_64_dump
	#objdump -D -Mintel,i386 -b binary -m i386 codefile_32 > codefile_32_dump


clean:
	rm -f a32.out a64.out codefile_32 codefile_64

