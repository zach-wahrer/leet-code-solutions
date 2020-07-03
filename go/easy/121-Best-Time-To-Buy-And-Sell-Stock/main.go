package main

import (
	"math"
)

func main() {

}

func getMaxProfit(prices []int) int {
	max_price := -1
	min_price := -1
	max_profit := 0

	for _, num := range prices {
		if num > max_price && min_price != -1 {
			max_price = num
			max_profit = int(math.Max(float64(max_profit), float64(max_price-min_price)))
		}

		if num < min_price || min_price == -1 {
			min_price = num
			max_price = -1
		}
	}

	return max_profit
}
