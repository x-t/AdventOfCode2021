from part1 import get_input, find_lowest_cost_path


def day15part2(filename: str) -> int:
    grid = get_input(filename)
    height = len(grid)
    width = len(grid[0])
    new_grid = [[0 for _ in range(width * 5)] for _ in range(height * 5)]
    # Copy old grid to new grid
    for y in range(height):
        for x in range(width):
            new_grid[y][x] = grid[y][x]
    for y in range(height):
        for x in range(width):
            for i in range(5):
                for j in range(5):
                    new_grid[y + height * i][x + j * width] = new_grid[y][x] + i + j
                    if new_grid[y + height * i][x + j * width] > 9:
                        new_grid[y + height * i][x + j * width] = new_grid[y + height * i][x + j * width] % 9

    go_from = (0, 0)
    go_to = (len(new_grid) - 1, len(new_grid[0]) - 1)

    cost_so_far = find_lowest_cost_path(go_from, go_to, new_grid)
    # for row in new_grid:
    #     print(row)
    return cost_so_far[go_to]


# Warning: this will not be fast.
if __name__ == '__main__':
    print(day15part2('input.txt'))
