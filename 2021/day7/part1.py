from typing import Callable


def day7part1(file_name: str) -> int:
    positions = read_input(file_name)
    return brute_force(positions, lambda x: abs(x))


def read_input(file_name: str) -> list[int]:
    with open(file_name, 'r') as f:
        return [int(x) for x in f.read().split(',')]


def brute_force(positions: list[int], sum_fn: Callable[[int], int]) -> int:
    fuels = []
    for i in range(max(positions) + 1):
        fuels_current = []
        for pos in positions:
            fuels_current.append(sum_fn(pos - i))
        fuels.append(sum(fuels_current))
    return min(fuels)


if __name__ == "__main__":
    print(day7part1('input.txt'))
