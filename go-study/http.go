package main

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"net/http"
	"os"
	"time"
)

func GetHttp() {
	resp, err := http.Get("http://www.google.com")
	if err != nil {
		panic(err)
	}

	// defer resp.Body.Close()

	// Print o status code
	fmt.Println("Response status:", resp.Status)

	req, err := http.NewRequest("GET", "http://www.google.com", nil)
	if err != nil {
		panic(err)
	}

	req.Header.Add("User-Agent", "myClient")
	req.Header.Set("Authorization", "123")

	resp, err = http.DefaultClient.Do(req)

	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()

	data, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(data))
}

func GetHttpWithCtx() {

	ctx := context.Background()
	ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
	defer cancel()

	req, err := http.NewRequestWithContext(ctx, "GET", "https://pokeapi.co/api/v2/pokemon", nil)
	if err != nil {
		panic(err)
	}

	req.Header.Add("User-Agent", "myClient")
	req.Header.Set("Authorization", "123")

	resp, err := http.DefaultClient.Do(req)

	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()

	data, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(data))
}

func PostHttp() {
	c := http.Client{}
	jsonVar := bytes.NewBuffer([]byte(`{"name": "wesley"}`))
	resp, err := c.Post("http://google.com", "application/json", jsonVar)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	io.CopyBuffer(os.Stdout, resp.Body, nil)
}
