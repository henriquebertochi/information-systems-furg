#include <stdio.h>

int fatorial(int x) {
    if (x == 0 || x == 1)
        return 1;
    else
        return x * fatorial(x - 1);
}

int main() {
    int x;
    
    printf("Digite um número inteiro para calcular o fatorial: ");
    scanf("%d", &x);
    
    if (x < 0) {
        printf("Erro: O fatorial de um número negativo não está definido.\n");
        return 1;
    }
    
    int resultado = fatorial(x);
    printf("%d! = %d\n", x, resultado);
    
    return 0;
}