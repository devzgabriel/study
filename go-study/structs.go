package main

import "fmt"

type Customer struct {
	Balance int64
}

type User struct {
	Name string
	ID   string
	// Embedded struct
	Customer
}

func (u *User) UpdateName(newName string) {

	fmt.Println("Updating name from", u.Name, "to", newName)

	u.Name = newName
}

func TestUser() {

	user := User{
		Name: "John",
		ID:   "123",
	}

	fmt.Println("User before update:", user)

	user.UpdateName("Doe")

	fmt.Println("User after update:", user)
}
