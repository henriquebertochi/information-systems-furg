.code
    lda n1
    sub n2
    jz IGUAL
    jlt CASO2

    lda n1
    sta max
    lda n2
    sta min
    jmp FIM

CASO2:
    lda n2
    sta max
    lda n1
    sta min

IGUAL:
FIM:
    hlt
.endcode

.data
    n1: db #03h
    n2: db #10h
    min: db #00h
    max: db #00h
.enddata

endereço de memoria	- valor	- var
0x0000	            - 03h   - n1
0x0001	            - 10h	- n2
0x0002	            - 03h	- min
0x0003	            - 10h   - max