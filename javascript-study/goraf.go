package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"time"
)

func main() {
	start := time.Now()

	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	fmt.Printf("Memory usage before allocation: %v MB\n", m.Alloc/1024/1024)

	rawSequences := make([]int, 10000000)
	for i := 0; i < 10000000; i++ {
		rawSequences[i] = i
	}

	runtime.ReadMemStats(&m)
	fmt.Printf("Memory usage after allocation: %v MB\n", m.Alloc/1024/1024)

	rand.Seed(time.Now().UnixNano())
	for i := len(rawSequences) - 1; i > 0; i-- {
		j := rand.Intn(i + 1)
		rawSequences[i], rawSequences[j] = rawSequences[j], rawSequences[i]
	}

	runtime.ReadMemStats(&m)
	fmt.Printf("Memory usage of array: %v MB\n", float64(len(rawSequences)*8)/1024/1024)

	elapsed := time.Since(start)
	fmt.Printf("Execution time: %s\n", elapsed)
}
