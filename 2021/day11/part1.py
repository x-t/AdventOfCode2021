def day11part1(filename: str) -> int:
    octopuses = get_input(filename)
    total = 0
    for i in range(100):
        octopuses = increment_layer(octopuses)
        octopuses, flashes, spots = flash_octopus(octopuses, [], [])
        # print(f"Step {i + 1}")
        # for row in range(len(octopuses)):
        #     for cell in range(len(octopuses[row])):
        #         if (row, cell) in spots:
        #             print(f"\033[1m{octopuses[row][cell]}\033[0m ", end='')
        #         else:
        #             print(f"{octopuses[row][cell]} ", end='')
        #     print()
        # print("-----------------------")
        # print(f"Flashes: {flashes}, total: {total}, spots: {spots}")
        total += flashes
    return total


def get_input(filename: str) -> list[list[int]]:
    _input = []
    with open(filename) as f:
        _input = f.read().splitlines()
    _input = [list(x) for x in _input]
    _input = [[int(x) for x in y] for y in _input]
    return _input


def increment_layer(layer: list[list[int]]) -> list[list[int]]:
    layer = [[y + 1 for y in x] for x in layer]
    return layer


def flash_octopus(layer: list[list[int]], increments=[], no_touch=[], total=0) -> (
        list[list[int]], int, list[(int, int)]):
    for r in range(len(layer)):
        for c in range(len(layer[r])):
            if layer[r][c] > 9:
                layer[r][c] = 0
                no_touch.append((r, c))
                total += 1
                # Add all adjacent cells to the list
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if 0 <= i < len(layer) and 0 <= j < len(layer[i]):
                            increments.append((i, j))
    for inc in increments:
        if inc not in no_touch:
            layer[inc[0]][inc[1]] += 1

    over_nine = 0
    for row in layer:
        for cell in row:
            if cell > 9:
                over_nine += 1
    if over_nine > 0:
        return flash_octopus(layer, [], no_touch, total)
    else:
        return layer, total, no_touch


if __name__ == "__main__":
    print(day11part1('input.txt'))
