"""
This is the individual-fish-tracking approach.
Do NOT use this part 2! You will absolutely fry your
computer. Part 2 is properly optimised.
"""


def day6part1():
    fishes = get_input()
    for i in range(18):
        print(f"Iteration {i}")
        fishes = day_pass(fishes)
    print(f"Answer: {len(fishes)}")
    return


def day_pass(fishes: list[int]) -> list[int]:
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes.append(8)
            fishes[i] = 6
            continue
        fishes[i] -= 1
    return fishes


def get_input() -> list[int]:
    f = open("inputs/day6.txt", "r").readlines()
    return [int(x) for x in f[0].split(',')]


if __name__ == '__main__':
    day6part1()
