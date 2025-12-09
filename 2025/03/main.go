package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func firstHighestNumber(numStr string, start, end int) int {
	bestIdx := start
	for i := start + 1; i < end; i++ {
		if numStr[bestIdx] == '9' {
			return bestIdx
		}
		if numStr[i] > numStr[bestIdx] {
			bestIdx = i
		}
	}
	return bestIdx
}

func solve(lines []string, digits int) int {
	total := 0
	for _, numStr := range lines {
		result := make([]byte, digits)
		lastIdx := -1

		for i := 0; i < digits; i++ {
			lastIdx = firstHighestNumber(numStr, lastIdx+1, len(numStr)-(digits-1-i))
			result[i] = numStr[lastIdx]
		}

		num, _ := strconv.Atoi(string(result))
		total += num
	}
	return total
}

func main() {
	data, _ := os.ReadFile("input.txt")
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")

	fmt.Println("Part 1:", solve(lines, 2))
	fmt.Println("Part 2:", solve(lines, 12))
}
