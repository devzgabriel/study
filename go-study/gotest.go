package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

func main() {
	myChan := make(chan int)
	go func() {
		for v := range myChan {
			if v != 0 {
				fmt.Printf("value is not 0: %d\n", v)
				continue
			}
			fmt.Println("value is 0")
		}
	}()

	myChan <- 42
	myChan <- 42
	myChan <- 0
	myChan <- 42
	close(myChan)

	fmt.Println("done")
}

type Message struct {
	Value int
}

func handle(ctx context.Context, m Message) error {
	fmt.Printf("Received message: %d", m.Value)
	return nil
}

func processMessages(ctx context.Context, msgs <-chan Message, workers int) error {
	line := make(chan struct{}, workers)
	var wg sync.WaitGroup

	for msg := range msgs {
		select {
		case <-ctx.Done():
			return nil
		case line <- struct{}{}:
		}

		wg.Add(1)
		go func(m Message) {
			defer wg.Done()
			defer func() { <-line }()

			ctxTimeout, cancel := context.WithTimeout(ctx, 5*time.Second)
			defer cancel()
			if err := handle(ctxTimeout, m); err != nil {
				fmt.Printf("error handling message")
			}
		}(msg)
	}

	wg.Wait()
	return nil
}
