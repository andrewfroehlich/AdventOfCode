package main

import (
	"fmt"
	"os"
	"strings"
)

type Coord struct {
	x, y int
}

var adjacency = []Coord{
	{-1, -1}, {-1, 0}, {-1, 1},
	{0, -1}, {0, 1},
	{1, -1}, {1, 0}, {1, 1},
}

func copyGrid(grid map[Coord]struct{}) map[Coord]struct{} {
	newGrid := make(map[Coord]struct{}, len(grid))
	for k := range grid {
		newGrid[k] = struct{}{}
	}
	return newGrid
}

func countAdjacent(coord Coord, grid map[Coord]struct{}) int {
	count := 0
	for _, adj := range adjacency {
		if _, exists := grid[Coord{coord.x + adj.x, coord.y + adj.y}]; exists {
			count++
		}
	}
	return count
}

func search(grid map[Coord]struct{}, maxAdjacent int, part2 bool) int {
	found := 0

	for {
		foundCoords := make(map[Coord]struct{})

		for coord := range grid {
			if countAdjacent(coord, grid) < maxAdjacent {
				foundCoords[coord] = struct{}{}
			}
		}

		if !part2 {
			return len(foundCoords)
		}

		if len(foundCoords) == 0 {
			return found
		}

		found += len(foundCoords)
		for coord := range foundCoords {
			delete(grid, coord)
		}
	}
}

func main() {
	data, _ := os.ReadFile("input.txt")
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")

	grid := make(map[Coord]struct{})
	for y, line := range lines {
		for x, char := range line {
			if char == '@' {
				grid[Coord{x, y}] = struct{}{}
			}
		}
	}

	fmt.Println("Part 1:", search(copyGrid(grid), 4, false))
	fmt.Println("Part 2:", search(copyGrid(grid), 4, true))
}
