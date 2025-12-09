package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type instruction struct {
	direction byte
	distance  int
}

func parseInput() []instruction {
	data, _ := os.ReadFile("input.txt")
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")

	instructions := make([]instruction, len(lines))
	for i, line := range lines {
		distance, _ := strconv.Atoi(line[1:])
		instructions[i] = instruction{line[0], distance}
	}
	return instructions
}

func updateDial(dial, distance int, direction byte) int {
	if direction == 'L' {
		return (dial - distance%100 + 100) % 100
	}
	return (dial + distance) % 100
}

func part1(instructions []instruction) int {
	dial, zeroes := 50, 0
	for _, inst := range instructions {
		dial = updateDial(dial, inst.distance, inst.direction)
		if dial == 0 {
			zeroes++
		}
	}
	return zeroes
}

func part2(instructions []instruction) int {
	dial, zeroes := 50, 0
	for _, inst := range instructions {
		if inst.direction == 'R' {
			zeroes += (dial + inst.distance) / 100
		} else {
			zeroes += inst.distance / 100
			if inst.distance%100 >= dial && dial > 0 {
				zeroes++
			}
		}
		dial = updateDial(dial, inst.distance, inst.direction)
	}
	return zeroes
}

func main() {
	instructions := parseInput()
	fmt.Println("Part 1:", part1(instructions))
	fmt.Println("Part 2:", part2(instructions))
}
