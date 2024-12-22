package main

import (
	"fmt"
	"strconv"
)

func TestArray() {
	for i, e := range "hello" {
		s := string(e)
		a := strconv.QuoteRuneToASCII(e)
		fmt.Println(i, e, s, a)
	}

	fmt.Println(string(65))
}
