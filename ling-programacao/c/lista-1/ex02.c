#include <stdio.h>

int main() {
    int n;
    printf("Digite um número inteiro positivo: ");
    scanf("%d", &n);

    if (n <= 1) {
        printf("%d não é primo.\n", n);
        return 0;
    }

    int i, primo = 1;

    for (i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            primo = 0;
            break;
        }
    }

    if (primo == 1)
        printf("%d é primo.\n", n);
    else
        printf("%d não é primo.\n", n);

    return 0;
}