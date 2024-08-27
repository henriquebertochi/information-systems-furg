function calcularMDC(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function calcularMMC(a, b) {
    return (a * b) / calcularMDC(a, b);
}

let num1 = parseInt(prompt("Digite o primeiro número:"));
let num2 = parseInt(prompt("Digite o segundo número:"));
let mmc = calcularMMC(num1, num2);
alert("O MMC de " + num1 + " e " + num2 + " é " + mmc);