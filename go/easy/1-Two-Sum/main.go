package main

func main() {

}

func twoSum(nums []int, target int) []int {
	compliments := make(map[int]int)

	for index, num := range nums {
		if val, ok := compliments[num]; ok {
			return []int{val, index}
		} else {
			compliments[target-num] = index
		}
	}
	return nil
}
