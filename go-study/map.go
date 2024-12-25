package main

import "fmt"

func StartMap() {
	mapByMake := make(map[string]string)
	mapByMake["name"] = "John"
	mapByMake["age"] = "20"

	mapByLiteral := map[string]string{
		"age": "20",
	}

	fmt.Println(mapByMake)
	fmt.Println(mapByLiteral)

	mapOfSlices := map[string][]int{
		"slice1": {1, 2, 3},
		"slice2": {4, 5, 6},
	}

	fmt.Println(mapOfSlices)

	_, ok := mapByMake["name"]
	fmt.Println("Does mapByMake has key 'name'?", ok)

	delete(mapByMake, "name")

	_, ok = mapByMake["name"]
	fmt.Println("Does mapByMake has key 'name' after delete?", ok)

	clear(mapByMake)
}

func LoopMap() {
	mapByMake := make(map[string]string)
	mapByMake["name"] = "John"
	mapByMake["age"] = "20"

	for k, v := range mapByMake {
		fmt.Println(k, v)
	}
}
