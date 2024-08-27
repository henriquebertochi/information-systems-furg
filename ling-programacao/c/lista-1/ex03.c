#include <stdio.h>

int main() {
    int n;
    
    printf("Digite um numero inteiro positivo: ");
    scanf("%d", &n);
    
    printf("Os primeiros %d numeros naturais impares sao:\n", n);
    
    int count = 0;
    int num = 1;
    
    while (count < n) {
        printf("%d ", num);
        num += 2;
        count++;
    }
    
    printf("\n");
    
    return 0;
}