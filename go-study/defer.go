package main

import "fmt"

func TestDefer() {

	x := doDefer()
	fmt.Println("x=", x)

}

func doDefer() int {

	fmt.Println("start")
	x := 5
	defer fmt.Println("defer 1 - " + fmt.Sprint(x))

	x = x + 10
	defer fmt.Println("defer 2 - " + fmt.Sprint(x))

	x = x + 100

	fmt.Println("end")
	return x
}
