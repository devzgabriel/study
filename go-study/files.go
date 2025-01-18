package main

import (
	"bufio"
	"fmt"
	"os"
)

func StudyFiles() {
	f, err := os.Create("test.txt")
	if err != nil {
		panic(err)
	}

	size, err := f.WriteString("Hello, World!\n")
	size, err = f.WriteString("Line 2\n")
	size, err = f.WriteString("Line 3\n")
	size, err = f.WriteString("Line 4\n")
	size, err = f.WriteString("Line 5\n")

	if err != nil {
		panic(err)
	}
	fmt.Printf("Wrote %d bytes\n", size)

	size, err = f.Write([]byte("Hello, World!"))
	if err != nil {
		panic(err)
	}
	fmt.Printf("Wrote %d bytes\n", size)

	f.Close()

	ar, err := os.ReadFile("test.txt")
	if err != nil {
		panic(err)
	}

	fmt.Println(string(ar))

	// Reading a file gradually
	c, err := os.Open("test.txt")
	if err != nil {
		panic(err)
	}

	reader := bufio.NewReader(c)
	buffer := make([]byte, 5)

	for {
		n, err := reader.Read(buffer)
		if err != nil {
			break
		}
		fmt.Println(string(buffer[:n]))
	}

	c.Close()

	// Reading a file line by line
	c, err = os.Open("test.txt")
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(c)
	fmt.Println("\n\nReading file line by line")

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

	c.Close()

	err = os.Remove("test.txt")

}
