package main

import "fmt"

type IPerson interface {
	Smile()
}

type Customer struct {
	Balance int64
	Active  bool
}

type User struct {
	Name string
	ID   string
	// Embedded struct
	customer Customer
}

func (u *User) UpdateName(newName string) {

	fmt.Println("Updating name from", u.Name, "to", newName)

	u.Name = newName
}

func (u *User) Smile() {
	fmt.Println("User is smiling")
}

func takePhoto(p IPerson) {
	p.Smile()
}

func TestUser() {

	user := User{
		Name: "John",
		ID:   "123",
	}

	user.customer = Customer{
		Balance: 100,
		Active:  true,
	}

	takePhoto(&user)

	fmt.Println("User before update:", user)

	user.UpdateName("Doe")

	fmt.Println("User after update:", user)
}
