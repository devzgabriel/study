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

func boundCheck(slice []int) {
	_ = slice[3] // bounds check once

	println(slice[0])
	println(slice[1])
	println(slice[2])
	println(slice[3])

}
