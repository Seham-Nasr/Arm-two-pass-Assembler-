# Arm-two-pass-Assembler-
A tool to convert an assembly language program  (32-bit Arm instruction set ) to machine code .
This project intent to design a two-pass assembler, which is a software or
program to convert an assembly language program to machine code. A
symbol table contains data respect to op-codes corresponding to the
mnemonics available in the instruction set architecture of the assembly
language and user-defined labels. Using symbol table, the tool being built
matches the op-code for each mnemonic that appears in the assembly
code and produces as output the equivalent machine code in the form of
object code or object listing.
Assembler runs in two passes. The first pass fills the symbol table with the
addresses of the user-defined labels calculated by the location counter.
The second pass output two machine code the object code and listing.
The two-pass assembler and GUI is implemented in Python, since Python
is a nifty language with a lot of text-processing and string-matching tools
and it’s ease in the Portability of programs.
