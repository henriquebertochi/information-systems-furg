package main

import "fmt"

func main() {
    n := 10
    contador := 0
    numero := 1

    for contador < n {
        fmt.Println(numero)
        numero += 2
        contador++
    }
}
