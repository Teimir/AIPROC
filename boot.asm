#рег 3 = рег 0 \ рег 1
#ВЫХОД ПО АДРЕСУ ИЗ СТЕКА
LABEL DIV:
LDR 2 1
SUB 0 1
POP 6

LABEL LOOP2:
ADD 3 2
SUB 0 1
POP 6
JFZ 0 6
JMP LOOP2

# рег 0 *= рег 1
#ВЫХОД ПО АДРЕСУ ИЗ СТЕКА
LABEL MUL:
LDR 2  1
MOV 0  3
SUB 1  2
POP 6
JFZ 1  6

# цикл умножения
LABEL LOOP:
ADD 0  3
SUB 1  2
POP 6 
JFZ 1  6  
JMP LOOP    


LABEL END:
HALT