package main

import "fmt"

type Animal interface {
	Sound() string
}

type Dog struct{}

func (d Dog) Sound() string {
	return "Woof"
}

type Cat struct{}

func (c Cat) Sound() string {
	return "Meow"
}

func TestInterface() {
	animals := []Animal{Dog{}, Cat{}}

	for _, animal := range animals {
		fmt.Println(animal.Sound())
	}
}

func TakeAnimal(a Animal) {
	switch a.(type) {
	case Dog:
		fmt.Println("It's a dog")
	case Cat:
		fmt.Println("It's a cat")
	default:
		fmt.Println("Unknown animal")
	}
}
