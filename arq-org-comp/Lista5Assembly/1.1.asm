.code
    lda A
    not
    add #01h
    add B
    jz FIM

INICIO:
    lda A
    add #01h
    sta A
    jmp INICIO

FIM:
    hlt
.endcode

.data
    A: db #00h
    B: db #05h
.enddata


; Endereço de memoria - valor - valor
; 0x0000              - 5     - A
; 0x0001              - 5     - B