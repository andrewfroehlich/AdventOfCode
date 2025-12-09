package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func usableFactors(n int) []int {
	var factors []int
	for i := 1; i <= n/2; i++ {
		if n%i == 0 {
			factors = append(factors, i)
		}
	}
	return factors
}

func parseRanges() [][2]int {
	data, _ := os.ReadFile("input.txt")
	parts := strings.Split(strings.TrimSpace(string(data)), ",")

	ranges := make([][2]int, len(parts))
	for i, part := range parts {
		fmt.Sscanf(part, "%d-%d", &ranges[i][0], &ranges[i][1])
	}
	return ranges
}

func part1() int {
	ranges := parseRanges()
	total := 0

	for _, r := range ranges {
		low, high := r[0], r[1]

		lowStr := strconv.Itoa(low)
		halfLen := len(lowStr) / 2
		pattern := lowStr[:halfLen]
		if pattern == "" {
			pattern = "0"
		}

		halfInt, _ := strconv.Atoi(pattern)
		current, _ := strconv.Atoi(pattern + pattern)

		for current <= high {
			if current >= low {
				total += current
			}
			halfInt++
			pattern = strconv.Itoa(halfInt)
			current, _ = strconv.Atoi(pattern + pattern)
		}
	}

	return total
}

func part2() int {
	ranges := parseRanges()
	invalidSet := make(map[int]bool)

	for _, r := range ranges {
		low, high := r[0], r[1]

		current := low
		for current <= high {
			currStr := strconv.Itoa(current)
			currLen := len(currStr)

			for _, factorSize := range usableFactors(currLen) {
				pattern := currStr[:factorSize]
				reps := currLen / factorSize

				patternInt, _ := strconv.Atoi(pattern)
				repeated, _ := strconv.Atoi(strings.Repeat(pattern, reps))

				for repeated <= high {
					if repeated >= low {
						invalidSet[repeated] = true
					}
					patternInt++
					pattern = strconv.Itoa(patternInt)
					repeated, _ = strconv.Atoi(strings.Repeat(pattern, reps))
				}
			}

			current = int(math.Pow10(currLen))
		}
	}

	total := 0
	for num := range invalidSet {
		total += num
	}

	return total
}

func main() {
	fmt.Println("Part 1:", part1())
	fmt.Println("Part 2:", part2())
}
