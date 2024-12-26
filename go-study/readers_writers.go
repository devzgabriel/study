package main

import (
	"errors"
	"fmt"
	"io"
	"strings"
)

func LearnReader() {
	str := "Hello, World!"
	// Read from stream into buffer
	reader := strings.NewReader(str)

	buffer := make([]byte, 5)
	n, err := reader.Read(buffer)
	if err != nil {
		panic(err)
	}

	fmt.Println(n)
	// Limit the number of bytes read from the stream because data is fewer than the possible buffer size
	fmt.Println(string(buffer[:n]))
}

func LearnReaderWithLoop() {
	str := "Hello, World!"
	// Read from stream into buffer
	reader := strings.NewReader(str)
	writer := MyWriter{}

	buffer := make([]byte, 2)

	for {
		n, err := reader.Read(buffer)
		if err != nil {
			if errors.Is(err, io.EOF) {
				break
			}
			panic(err)
		}

		if n == 0 {
			break
		}

		// fmt.Println(n)
		// fmt.Println(string(buffer[:n]))
		writer.Write(buffer[:n])
	}
}

type MyWriter struct {
}

func (w MyWriter) Write(p []byte) (n int, err error) {
	fmt.Print(string(p))
	return len(p), nil
}
