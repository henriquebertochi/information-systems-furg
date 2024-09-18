.code
    ; inicia os reg
    lda A            ; carrega o A no acumulador
    sta TEMP_A       ; armazena temp o A
    lda B            ; carrega o B no acumulador
    sta TEMP_B       ; armazena temp o B
    lda #00h         ; inicia o result como 0
    sta RESULTADO    ; armazena o result da multip
                                                                        
MULTIPLICACAO_LOOP:
    lda TEMP_B       ; carrega TEMP_B no acumulador
    jz ZERO          ; se o acumulador for 0(TEMP B = 0), vai ir para ZERO
                                                                         
    ; adiciona TEMP_A ao RESULTADO
    lda RESULTADO    ; carrega o RESULTADO no acumulador
    add TEMP_A       ; adiciona TEMP_A ao acumulador
    sta RESULTADO    ; armazena o result da soma em RESULTADO

    ; decrementa TEMP_B
    lda TEMP_B       ; carrega TEMP_B no acumulador
    add #FFh         ; subtrai 1 do TEMP_B                 
    sta TEMP_B       ; att TEMP_B

    jmp MULTIPLICACAO_LOOP ; continua o loop
                                    
ZERO:                                                                 
    hlt              ; encerra o programa
                                                                
.endcode

.data
    A: db #08h       ; valor do primeiro número (8)
    B: db #00h       ; valor do segundo número (0) 
    TEMP_A: db #00h  ; armazena o A                                       
    TEMP_B: db #00h  ; armazena o B
    RESULTADO: db #00h ; armazena o result da multip
.enddata                                                    
