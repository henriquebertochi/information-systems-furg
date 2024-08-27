// Para esse exercício precisei pesquisar sobre as bibliotecas uteis para manipulação de strings

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var frase, palavra string

	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("Digite a frase: ")
	scanner.Scan()
	frase = scanner.Text()

	fmt.Print("Digite a palavra a ser contada: ")
	scanner.Scan()
	palavra = scanner.Text()

	numOcorrencias := strings.Count(frase, palavra)

	fmt.Printf("Temos que a palavra '%s' ocorre %d vezes na frase.\n", palavra, numOcorrencias)
}