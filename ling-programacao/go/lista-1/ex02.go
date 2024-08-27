package main

import (
    "fmt"
)

func Primo(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func main() {
    n := 29
    if Primo(n) {
        fmt.Printf("%d é primo\n", n)
    } else {
        fmt.Printf("%d não é primo\n", n)
    }
}
