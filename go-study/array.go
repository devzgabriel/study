package main

import (
	"fmt"
	"strconv"
)

func TestArray() {
	for idx, ascCode := range "hello" {
		s := string(ascCode)
		a := strconv.QuoteRuneToASCII(ascCode)
		fmt.Println(idx, ascCode, s, a)
	}

	fmt.Println("string(65) == string(rune(65)):", string(65), string(rune(65)))
}

func boundCheck(slice []int) {
	_ = slice[3] // bounds check once

	println(slice[0])
	println(slice[1])
	println(slice[2])
	println(slice[3])

}
