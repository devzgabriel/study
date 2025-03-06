package main

type Product struct {
	Name  string
	Price float64
}

func newProduct(name string, price float64) *Product {
	return &Product{
		Name:  name,
		Price: price,
	}
}

func main() {
	// quantity, _ := strconv.Atoi("10")
	// println(quantity)

	// B3Report()

	product := newProduct("Product 1", 10.0)
	println(product, &product, &product.Name, &product.Price)
	// product2 := newProduct("Product 2", 20.0)
	// println(product2, &product2)
}
