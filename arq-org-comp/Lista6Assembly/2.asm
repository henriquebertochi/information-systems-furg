.code
    ComparaAB:
        lda A
        not
        add #01h
        add B
        jn AmaiorB
        
    BmaiorA:
        lda B
        sta MAIOR
        jmp ComparaC

    AmaiorB:
        lda A
        sta MAIOR
        lda B
        sta MENOR

    ComparaC:
        lda C
        not
        add #01h
        add C
        jn CmenorMENOR

    CmaiorMENOR:
        lda C
        sta MEDIO
        jmp COND1

    CmenorMENOR:
        lda MENOR
        sta MEDIO
        lda C
        sta MENOR
        jmp COND1

    CmaiorMAIOR:
        lda MAIOR
        sta MEDIO
        lda C
        sta MAIOR

    COND1:
        lda MAIOR
        not
        add #01h
        add MENOR
        add MEDIO
        jn FIM

    COND2:
        lda MEDIO
        not
        add #01h
        add MAIOR
        not
        add #01h
        add MENOR
        jn FIM

    VERDADE:
        lda #01h
        sta SIM

    FIM:
        hlt
.endcode

.data
    A: db #06h
    B: db #08h
    C: db #04h
    MAIOR: db #00h
    MEDIO: db #00h
    MENOR: db #00h
    SIM: db #00h
.enddata
