package main
import "fmt"

func potencia(base int, expoente int) int {
    resultado := 1
    for expoente > 0 {
        if expoente % 2 == 1 {
            resultado *= base
        }
        base *= base
        expoente /= 2
    }
    return resultado
}

func main() {
    base := 2
    expoente := 3
    fmt.Printf("%d^%d = %d\n", base, expoente, potencia(base, expoente))
}