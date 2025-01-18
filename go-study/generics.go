package main

// ~ significa que a interface aceita aquele tipo, mas também outros tipos que tenham como core aquele tipo
type Signed interface {
	~int8 | ~int16 | ~int32 | ~int64
}

type Unsigned interface {
	~uint8 | ~uint16 | ~uint32 | ~uint64
}

type Integer interface {
	Signed | Unsigned
}

//  ----------------------------

type gasEngine struct {
	gallons int
	mpg     int
}

type electricEngine struct {
	kWh   int
	mpkWh int
}

type car[T gasEngine | electricEngine] struct {
	carMake  string
	carModel string
	engine   T
}

func Somar[T int | float64](a, b T) T {
	return a + b
}
