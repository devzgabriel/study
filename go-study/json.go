package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Person struct {
	Name string
	Age  int
}

func StudyJson() {
	// Marshal
	p := Person{"Tom", 20}
	b, err := json.Marshal(p)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Marshal:", string(b))
	// fmt.Println(string(b))

	// Unmarshal
	var p1 Person
	err = json.Unmarshal(b, &p1)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Unmarshal:", p1)

	// Encode
	p2 := Person{"Alice", 30}
	enc := json.NewEncoder(os.Stdout)
	err = enc.Encode(p2)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Decode
	var p3 Person

	fmt.Println("Enter a JSON object:")
	dec := json.NewDecoder(os.Stdin)
	err = dec.Decode(&p3)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Decode:", p3)

}
