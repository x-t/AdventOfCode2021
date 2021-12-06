"""
This is the individual-fish-tracking approach.
Do NOT use this part 2! You will absolutely fry your
computer. Part 2 is properly optimised.
"""


def day6part1(file_name: str) -> int:
    fishes = get_input(file_name)
    for i in range(80):
        fishes = day_pass(fishes)
    return len(fishes)


def day_pass(fishes: list[int]) -> list[int]:
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes.append(8)
            fishes[i] = 6
            continue
        fishes[i] -= 1
    return fishes


def get_input(file_name: str) -> list[int]:
    with open(file_name, 'r') as f:
        data = f.readlines()
    res = [int(x) for x in data[0].split(',')]
    return res


if __name__ == '__main__':
    print(day6part1('input.txt'))
