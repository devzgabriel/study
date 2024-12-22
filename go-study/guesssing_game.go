package main

import (
	"bufio"
	"fmt"
	"math/rand/v2"
	"os"
	"strconv"
	"strings"
)

func GuessingGame() {
	fmt.Println("Jogo da Adivinhação")
	fmt.Println("Um número será sorteado. Tente acertar. O número é um inteiro entre 1 e 100.")

	// Sorteia um número positivo entre 1 e 100
	x := rand.Int64N(101)

	// Cria um scanner para ler a entrada do usuário
	scanner := bufio.NewScanner(os.Stdin)
	guesses := [10]int64{}

	for i := range guesses {
		fmt.Println("Digite um número:")
		scanner.Scan()

		guess := scanner.Text()

		// Sanitizar o input (tirar espaços em branco)
		guess = strings.TrimSpace(guess)

		guessAsInt, err := strconv.ParseInt(guess, 10, 64)

		if err != nil {
			fmt.Println("Por favor, digite um número válido.")
			continue
		}

		switch {
		case guessAsInt < x:
			fmt.Println("O número é maior que", guessAsInt)
		case guessAsInt > x:
			fmt.Println("O número é menor que", guessAsInt)
		case guessAsInt == x:
			fmt.Printf(
				"Parabéns, o número era: %d\n"+
					"Voce tentou %d vezes\n"+
					"Você tentou os números: %v\n",
				x, i+1, guesses[:i],
			)
			return
		}

		guesses[i] = guessAsInt
	}

	// Só temos custo de performance se as strings fossem variáveis
	// mas como são constantes, não há custo por serem resolvidas em tempo de compilação
	fmt.Printf(
		"Você não acertou. O número era %d\n"+
			"Você tentou os números:\n"+
			"%v\n",
		x, guesses,
	)
}
