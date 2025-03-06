package main

import (
	"context"
	"encoding/csv"
	"fmt"
	"log/slog"
	"os"
	"strconv"
	"strings"
)

func B3Report() {
	file, err := os.Open("b3_file.csv")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer file.Close()

	reader := csv.NewReader(file)
	records, err := reader.ReadAll()
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	type ProductData struct {
		totalQuantity int
		totalValue    float64
		profit        float64
		loss          float64
		totalSpent    float64
		totalSold     float64
	}

	productData := make(map[string]*ProductData)

	for _, record := range records[1:] {
		product := strings.Split(record[3], " - ")[0]
		if _, exists := productData[product]; !exists {
			productData[product] = &ProductData{}
		}

		quantity, _ := strconv.Atoi(record[5])
		priceStr := strings.Map(func(r rune) rune {
			if r >= '0' && r <= '9' {
				return r
			}
			return -1
		}, record[6])
		price, _ := strconv.ParseFloat(priceStr, 64)
		valueStr := strings.Map(func(r rune) rune {
			if r >= '0' && r <= '9' {
				return r
			}
			return -1
		}, record[7])
		value, _ := strconv.ParseFloat(valueStr, 64)

		slog.Log(
			context.Background(),
			slog.LevelInfo, "new record",
			"quantity", quantity,
			"price", price,
			"value", value,
		)

		if record[0] == "Credito" {
			productData[product].totalQuantity += quantity
			productData[product].totalValue += value
			productData[product].totalSpent += value
		} else if record[0] == "Debito" {
			mediumPrice := productData[product].totalValue / float64(productData[product].totalQuantity)
			if price > mediumPrice {
				productData[product].profit += (price - mediumPrice) * float64(quantity)
			} else {
				productData[product].loss += (mediumPrice - price) * float64(quantity)
			}
			productData[product].totalQuantity -= quantity
			productData[product].totalValue -= value
			productData[product].totalSold += value
		}
	}

	for product, data := range productData {
		fmt.Printf("Product: %s\n", product)
		fmt.Printf("  Medium Price: R$ %.2f\n", data.totalValue/float64(data.totalQuantity)/100)
		fmt.Printf("  Profit: R$ %.2f\n", data.profit/100)
		fmt.Printf("  Loss: R$ %.2f\n", data.loss/100)
		fmt.Printf("  Total Spent: R$ %.2f\n", data.totalSpent/100)
		fmt.Printf("  Total Sold: R$ %.2f\n", data.totalSold/100)
		fmt.Printf("  In box: R$ %.2f\n", ((-data.totalSpent)-(-data.totalSold))/100)

	}
}
