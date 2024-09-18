.code
lda  # 00h
sta i
lda  # 00h
sta X

INICIO:
    lda i
    add N
    jz FIM

    lda i
    add i
    add i
    lda X
    add i
    sta X

    lda i
    add  # 01h
    sta i

    jmp INICIO

FIM:
    hlt
.endcode

.data
i: db  # 00h
X: db  # 00h
N: db  # 05h
.enddata


endereço de memoria - valor - val

0x0000 - 05h - i

0x0001 - 14h - X

0x0002 - 05h - N
