public class MMC {
    public static void main(String[] args) throws java.io.IOException {
        java.io.BufferedReader reader = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));

        System.out.println("Digite o primeiro número:");
        int num1 = Integer.parseInt(reader.readLine());
        System.out.println("Digite o segundo número:");
        int num2 = Integer.parseInt(reader.readLine());

        int mmc = calcularMMC(num1, num2);
        System.out.println("O MMC de " + num1 + " e " + num2 + " é " + mmc);
    }

    public static int calcularMMC(int a, int b) {
        return (a * b) / calcularMDC(a, b);
    }

    public static int calcularMDC(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}