package main

import (
	"math"
)

func main() {

}

func getMaxProfit(prices []int) int {
	max_price := math.Inf(-1)
	min_price := math.Inf(1)
	max_profit := 0.0

	for _, num := range prices {
		if float64(num) > max_price && min_price != math.Inf(-1) {
			max_price = float64(num)
			max_profit = math.Max(max_profit, max_price-min_price)
		}

		if float64(num) < min_price || min_price == math.Inf(-1) {
			min_price = float64(num)
			max_price = math.Inf(-1)
		}
	}

	return int(max_profit)
}
