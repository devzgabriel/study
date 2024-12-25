package main

func Pointers() {
	x := 10
	p := &x

	println("The value of x is: ", x)
	println("The value of pointer p is: ", p)
	println("The value of *p reference is: ", *p, "(Equivalent to x)")

	notChangeX(x)
	println("After notChangeX, the value of x still is: ", x)

	// changeX(p)
	changeX(&x)
	println("After changeX, the value of x is: ", x)
}

func notChangeX(x int) {
	x = 20
}

func changeX(x *int) {
	*x = 20
}
