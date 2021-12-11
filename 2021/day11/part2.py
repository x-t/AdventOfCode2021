from part1 import get_input, increment_layer, flash_octopus


def day11part2(filename: str) -> int:
    octopuses = get_input(filename)
    i = 0
    while True:
        i += 1
        octopuses = increment_layer(octopuses)
        octopuses, flashes, spots = flash_octopus(octopuses, [], [])
        if len(spots) == 100:
            return i


if __name__ == "__main__":
    print(day11part2('input.txt'))
