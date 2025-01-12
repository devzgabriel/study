package main

import "fmt"

func TestTypeAssertion() {

	var i interface{} = "hello"

	s, ok := i.(string)
	fmt.Printf("Converted value is %q and ok %v\n", s, ok)

	f, ok := i.(float64)
	fmt.Printf("Converted value is %f and ok %v\n", f, ok)

	// panic: interface conversion: interface {} is string, not float64
	// f = i.(float64)
	// fmt.Println(f)
}
