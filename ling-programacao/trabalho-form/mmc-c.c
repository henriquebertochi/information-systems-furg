int calcularMDC(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int calcularMMC(int a, int b) {
    return (a * b) / calcularMDC(a, b);
}

int main() {
    int num1 = 12;
    int num2 = 18;
    
    int mmc = calcularMMC(num1, num2);
    printf("O MMC de %d e %d é %d\n", num1, num2, mmc);
    
    return 0;
}