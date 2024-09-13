.code
    lda N
    sub M
    jz EHMULT
    jn FIM

    lda N
    sub M
    sta N
    jmp INICIO

EHMULT:
    lda #01h
    sta SIM

FIM:
    hlt
.endcode

.data
    M: db #04h
    N: db #08h
    SIM: db #00h
.enddata

endereço de memoria	- valor	- var
0x0000	            - 03h   - n1
0x0001	            - 10h	- n2
0x0002	            - 03h	- min
0x0003	            - 10h   - max