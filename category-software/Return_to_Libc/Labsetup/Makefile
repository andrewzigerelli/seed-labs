TARGET = retlib 

all: ${TARGET}

N = 12
retlib: retlib.c retlib2
	#gcc -m32 -DBUF_SIZE=${N} -fno-stack-protector -z noexecstack -o $@ $@.c
	gcc -g -DBUF_SIZE=${N} -fno-stack-protector -z noexecstack -o $@ $@.c
	#sudo chown root $@ && sudo chmod 4755 $@

retlib2: retlib.c
	#gcc -m32 -DBUF_SIZE=${N} -fno-stack-protector -z noexecstack -o $@ $@.c
	gcc -DBUF_SIZE=${N} -fno-stack-protector -z noexecstack -o $@ $<
	#sudo chown root $@ && sudo chmod 4755 $@

clean:
	rm -f *.o *.out ${TARGET} badfile
