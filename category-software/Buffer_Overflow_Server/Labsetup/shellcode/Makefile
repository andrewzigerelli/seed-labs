
all: 
	gcc -z execstack -o a64.out call_shellcode.c
	#gcc -m32 -z execstack -o a32.out call_shellcode.c

asm:
	objdump -D -Mintel,x86-64 -b binary -m i386:x86-64 codefile_64 > codefile_64_dump
	#objdump -D -Mintel,i386 -b binary -m i386 codefile_32 > codefile_32_dump

debug:
	gcc -g -z execstack -o a64_debug.out call_shellcode.c

res2:
	objdump -D -Mintel,x86-64 -b binary -m i386:x86-64 res2.bin > res2.dump

asm65:
	objdump -D -Mintel,x86-64 -b binary -m i386:x86-64 codefile_65 > codefile_65_dump

tiny:
	objdump -D -Mintel,x86-64 -b binary -m i386:x86-64 codefile_64_tiny > codefile_64_tiny_dump

custom_asm:
	nasm custom_shellcode.s -o mysh_64
	#ld mysh_64.o -o mysh_64
	#nasm -f elf64 custom_shellcode.s -l listing.lst
	objdump -D -Mintel,x86-64 -b binary -m i386:x86-64 mysh_64 > mysh_64_dump


clean:
	rm -f a32.out a64.out codefile_32 codefile_64
