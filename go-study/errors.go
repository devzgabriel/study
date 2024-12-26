package main

import (
	"errors"
	"fmt"
)

type SqrtError struct {
	msg string
}

func (e SqrtError) Error() string { return e.msg }

var (
	ErrNotFound = errors.New("Not found error")
	SomeErr     = errors.New("Some error 1")
	SomeErr2    = errors.New("Some error 2")
)

func getErr() error { return nil }
func a() error      { return SomeErr }
func b() error      { return SomeErr2 }

func Sqrt(f float64) (float64, error) {
	if f < 0 {
		return 0, SqrtError{"Cannot Sqrt negative number"}
	}
	return f, nil
}

func TestSqrt() {
	r, err := Sqrt(-10)

	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(r)
}

func LearnErr() {
	err := getErr()

	if err == nil {
		fmt.Println("No error")
		return
	}

	// Check if error is of type SqrtError
	// if _, ok := err.(SqrtError); ok {}
	var sqrtErr SqrtError
	if errors.As(err, &sqrtErr) {
		fmt.Println(sqrtErr)
		return
	}

	if errors.Is(err, ErrNotFound) {
		fmt.Println(err)
		return
	}

	fmt.Println("Other error", err)
}

func JoinErr() error {
	var errResult error
	err1 := a()
	err2 := b()

	if err1 != nil {
		errResult = errors.Join(errResult, err1)
	}

	if err2 != nil {
		errResult = errors.Join(errResult, err2)
	}

	return errResult
}

func LearnJoinErr() {
	err := JoinErr()
	if err != nil {
		fmt.Println(err)
		fmt.Println(errors.Is(err, SomeErr))
		fmt.Println(errors.Is(err, SomeErr2))
	}
}
