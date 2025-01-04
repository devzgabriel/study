package main

import (
	"fmt"
	"time"
)

// Recebe um chan apenas para escrever
func runner(ch chan<- int, id int) {
	fmt.Println("Runner started", id)
	time.Sleep(2 * time.Second)
	for {
		fmt.Printf("Runner %d sending data\n", id)
		ch <- id
		fmt.Printf("Runner %d sent data\n", id)
		// time.Sleep(1 * time.Second)
	}
}

func StudyChan() {
	// To implement buffer, use ch := make(chan int, 4)
	ch := make(chan int)

	go runner(ch, 1)
	go runner(ch, 2)
	go runner(ch, 3)
	go runner(ch, 4)

	for {
		num, ok := <-ch
		fmt.Printf("num=%d, ok=%v\n", num, ok)
		time.Sleep(3 * time.Second)
	}
}
