#include <stdio.h>

int meuStrlen(char str[]) {
    int len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}

int meuStrncmp(char str1[], char str2[], int n) {
    for (int i = 0; i < n; i++) {
        if (str1[i] != str2[i]) {
            return str1[i] - str2[i];
        }
        if (str1[i] == '\0' || str2[i] == '\0') {
            break;
        }
    }
    return 0;
}

int contarPalavraNaFrase(char frase[], char palavra[]) {
    int count = 0;
    int palavra_len = meuStrlen(palavra);
    int frase_len = meuStrlen(frase);

    for (int i = 0; i <= frase_len - palavra_len; i++) {
        if (meuStrncmp(&frase[i], palavra, palavra_len) == 0) {
            count++;
        }
    }
    
    return count;
}

int main() {
    char frase[100];
    char palavra[20];
    
    printf("Digite a frase: ");
    fgets(frase, sizeof(frase), stdin);
    frase[strcspn(frase, "\n")] = '\0';

    printf("Digite a palavra: ");
    fgets(palavra, sizeof(palavra), stdin);
    palavra[strcspn(palavra, "\n")] = '\0';
    
    int ocorrencias = contarPalavraNaFrase(frase, palavra);
    
    printf("Temos que a palavra %s ocorre %d vezes na frase.\n", palavra, ocorrencias);
    
    return 0;
}