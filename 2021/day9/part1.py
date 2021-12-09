def day9part1(filename: str) -> int:
    _input = get_input(filename)
    low_points = find_low_points(_input)
    low_point_values = []
    for point in low_points:
        low_point_values.append(_input[point[1]][point[0]])
    return len(low_points) + sum(low_point_values)


def find_low_points(heightmap: list[list[int]]) -> list[list[int]]:
    low_points = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            check_up, check_left, check_right, check_down = True, True, True, True
            needed_to_be_low = 4
            lower_on = 0
            # Top half
            if y == 0:
                check_up = False
                needed_to_be_low -= 1
            # Bottom half
            if y == len(heightmap) - 1:
                check_down = False
                needed_to_be_low -= 1
            # Left half
            if x == 0:
                check_left = False
                needed_to_be_low -= 1
            # Right half
            if x == len(heightmap[y]) - 1:
                check_right = False
                needed_to_be_low -= 1
            # Check if the current point is a low point
            if check_up and heightmap[y - 1][x] > heightmap[y][x]:
                lower_on += 1
            if check_left and heightmap[y][x - 1] > heightmap[y][x]:
                lower_on += 1
            if check_right and heightmap[y][x + 1] > heightmap[y][x]:
                lower_on += 1
            if check_down and heightmap[y + 1][x] > heightmap[y][x]:
                lower_on += 1
            if lower_on >= needed_to_be_low:
                low_points.append([x, y])
    return low_points


def get_input(filename: str) -> list[list[int]]:
    _input = []
    with open(filename) as f:
        _input = f.read().splitlines()
    _input = [list(x) for x in _input]
    _input = [[int(x) for x in line] for line in _input]
    return _input


if __name__ == "__main__":
    print(day9part1("input.txt"))
