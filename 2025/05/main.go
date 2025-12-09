package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Range struct {
	low, high int
}

func parse() ([]Range, []int) {
	data, _ := os.ReadFile("input.txt")
	parts := strings.Split(string(data), "\n\n")

	var ranges []Range
	for _, line := range strings.Split(strings.TrimSpace(parts[0]), "\n") {
		var r Range
		fmt.Sscanf(line, "%d-%d", &r.low, &r.high)
		ranges = append(ranges, r)
	}

	var ids []int
	for _, line := range strings.Split(strings.TrimSpace(parts[1]), "\n") {
		id, _ := strconv.Atoi(line)
		ids = append(ids, id)
	}

	return ranges, ids
}

func isFresh(num int, ranges []Range) bool {
	for _, r := range ranges {
		if r.low <= num && num <= r.high {
			return true
		}
	}
	return false
}

func part1(ranges []Range, ids []int) int {
	count := 0
	for _, id := range ids {
		if isFresh(id, ranges) {
			count++
		}
	}
	return count
}

func part2(ranges []Range) int {
	sorted := make([]Range, len(ranges))
	copy(sorted, ranges)
	sort.Slice(sorted, func(i, j int) bool {
		return sorted[i].low < sorted[j].low
	})

	merged := []Range{sorted[0]}

	for _, r := range sorted[1:] {
		last := &merged[len(merged)-1]
		if r.low <= last.high+1 {
			last.high = max(last.high, r.high)
		} else {
			merged = append(merged, r)
		}
	}

	total := 0
	for _, r := range merged {
		total += r.high - r.low + 1
	}
	return total
}

func main() {
	ranges, ids := parse()
	fmt.Println("Part 1:", part1(ranges, ids))
	fmt.Println("Part 2:", part2(ranges))
}
