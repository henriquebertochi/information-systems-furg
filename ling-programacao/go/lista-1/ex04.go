package main

import "fmt"

func Conversao(fahrenheit float64) float64 {
    celsius := (fahrenheit - 32) * 5 / 9
    return celsius
}

func main() {
    var fahrenheit float64
    fmt.Print("Digite a temperatura em Fahrenheit: ")
    fmt.Scan(&fahrenheit)

    celsius := Conversao(fahrenheit)
    fmt.Printf("A temperatura em Celsius é: %.2f\n", celsius)
}