from part1 import read_input, brute_force


def day7part2(file_name: str) -> int:
    positions = read_input(file_name)
    return brute_force(positions, lambda x: arithmetic_sum(abs(x)))


def arithmetic_sum(n: int) -> int:
    return n * (n + 1) // 2


if __name__ == "__main__":
    print(day7part2('input.txt'))
