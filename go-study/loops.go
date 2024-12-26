package main

import (
	"fmt"
	"sync"
)

func LearnLoops() {
	// Init statement, condition, post statement
	for i := 0; i < 10; i++ {
	}

	// Os params do for são opcionais
	i := 0
	for i < 10 {
		fmt.Println(i)
		i++
	}

	// Loop infinito
	for {
		break
	}

	// Loops com range podem declarar nenhuma, uma ou duas variáveis
	arr := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

	for idx, elem := range arr {
		fmt.Println(idx, elem)
	}
}

func LearnLoopsWg() {
	// Testa concorrência da versão 1.21 para 1.22
	// onde os endereços de memória são atualizados a cada loop
	// ao invés de manterem fixos e causarem bugs

	// Print concorrentemente o index do loop, usando wp pra esperar as threads paralelas
	const n = 10
	var wg sync.WaitGroup
	wg.Add(10)

	for i := 0; i < n; i++ {
		go func() {
			defer wg.Done()
			// Isso é um problema de condição de corrida
			// Tem mais de uma thread lendo ou alterando uma variável ao msm tempo
			fmt.Println(i)
		}()
	}

	wg.Wait()
}
