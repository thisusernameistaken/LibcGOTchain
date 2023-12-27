# Libc GOT chain gadget finder

Example:
```
0xb1880: endbr64 ; push r14; mov  r14, rdx; push r13; mov  r13, rsi; push r12; mov  r12, rdi; push rbp; sub  rsp, 0x8; call sub_28490; mov  rsi, r14; mov  rdi, r13; lea  rbp, [r12+rax]; call jump_strnlen; 
0xebe50: lea  rdi, [rel 0x1d82c9]  {"PATH"}; call getenv; mov  esi, 0xff; mov  rdi, r15; test rax, rax; mov  r14, rax; lea  rax, [rel 0x1d9cc3]  {"/bin:/usr/bin"}; cmove   r14, rax; call jump_strnlen; 
0xebe50: lea  rdi, [rel 0x1d82c9]  {"PATH"}; call getenv; mov  esi, 0xff; mov  rdi, r15; test rax, rax; mov  r14, rax; lea  rax, [rel 0x1d9cc3]  {"/bin:/usr/bin"}; cmove   r14, rax; call jump_strnlen; mov  esi, 0xfff; mov  rbx, rax; mov  rdi, r14; call jump_strnlen; 
0xb18d0: endbr64 ; push r13; mov  r13, rsi; mov  rsi, rdx; push r12; push rbp; mov  rbp, rdx; push rbx; mov  rbx, rdi; mov  rdi, r13; sub  rsp, 0x8; call jump_strnlen; 
0xb1940: endbr64 ; push r13; mov  r13, rdi; push r12; push rbp; mov  rbp, rsi; mov  rsi, rdx; push rbx; mov  rdi, rbp; mov  rbx, rdx; sub  rsp, 0x8; call jump_strnlen; 
0xd32ee: mov  rdi, r15; call jump_strnlen; 
0xf02b0: push r14; mov  r14, rdi; push r13; push r12; push rbp; mov  rbp, rsi; push rbx; mov  rbx, rdx; sub  rsp, 0x30; mov  r13, qword [rsi+0x8]; mov  qword [rsp+0x8], rdi; lea  r12, [rsp+0x20]; shr  r13, 0x2; lea  rsi, [r13-0x1]; mov  rax, qword [fs:0x28]; mov  qword [rsp+0x28], rax; xor  eax, eax; mov  qword [rsp+0x20], 0x0; call jump_strnlen; 
0x10e8f0: mov  rsi, r12; sub  rsi, rdi; mov  rdi, r14; sub  rsi, 0x1; call jump_strnlen; 
0xa8daf: mov  rsi, qword [rsp+0x20]; lea  rdi, [r14+r13]; mov  qword [rsp+0x10], r8; mov  qword [rsp+0x8], rcx; mov  qword [rsp], rdx; call jump_strnlen; 
0xa8f4c: mov  rsi, qword [rsp+0x10]; lea  rdi, [r14+r13]; mov  qword [rsp+0x8], rcx; mov  qword [rsp], r8; call jump_strnlen; 
0xa90b1: mov  rdi, r13; call sub_28490; mov  rdi, r12; mov  rsi, rax; mov  qword [rsp+0x8], rax; mov  r14, rax; or   rsi, 0x200; call jump_strnlen; 
0xa9262: mov  rax, qword [rsp+0x8]; mov  esi, 0x800; lea  rdi, [r15+rax]; call jump_strnlen; 
0x7594b: movsxd  rsi, r14d; mov  rdi, r15; call jump_strnlen; 
0x73970: movsxd  rsi, r11d; mov  rdi, r12; call jump_strnlen; 
0x2c57c: mov  r15, r8; mov  rdi, r12; mov  qword [rbp-0x80], r10; sub  r15, r12; mov  qword [rbp-0x78], r9; mov  rsi, r15; mov  qword [rbp-0x70], rcx; mov  qword [rbp-0x68], r11; mov  qword [rbp-0x60], r8; call jump_strnlen; 
0xc67d8: mov  rbx, qword [rsi]; mov  r15, rdi; mov  r13, rsi; lea  rsi, [rdx-0x1]; mov  r14, rcx; mov  rdi, rbx; call jump_strnlen; 
0x171de3: mov  rax, qword [rsp+0x8]; mov  esi, 0x20; lea  r14, [rax+0x2c]; mov  rdi, r14; call jump_strnlen; 
0xa8630: endbr64 ; push r12; push rbp; mov  rbp, rdi; sub  rsp, 0x8; call jump_strnlen; 
0x44cb9: mov  rsi, r12; mov  rdi, r13; call jump_strnlen;
```
overwrite multple libc got entries and chain them together to get what you want
