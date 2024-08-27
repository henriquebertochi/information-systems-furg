#include <stdio.h>

int main() {
    float temperatura_fahrenheit, temperatura_celsius;

    printf("Digite a temperatura em Fahrenheit: ");
    scanf("%f", &temperatura_fahrenheit);

    temperatura_celsius = (temperatura_fahrenheit - 32) * 5 / 9;

    printf("%.2f Fahrenheit equivale a %.2f Celsius.\n", temperatura_fahrenheit, temperatura_celsius);

    return 0;
}