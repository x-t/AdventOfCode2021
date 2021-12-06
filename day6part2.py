"""
This optimisation task is pretty simple, although admittedly not
the most obvious. In part 1, we tracked individual fish, the
fish array can be written as this:
        F[N] = 0..=8
          ^    ^--- Fish's cycle
          Fish
All we have to do is flip the array
        F[0..=8] = N
          ^        ^------ Fish
          Fish's cycle
To get the total amount of fish in the first array, we take the
length of F[N], to get the total amount of fish in the second array,
we take the sum of F[0..=8].
"""

from day6part1 import get_input


def day6part2():
    fishes = get_input()
    days = convert_to_days(fishes)
    for i in range(256):
        days = day_pass(days)
    print(f"Answer: {sum(days)}")


def convert_to_days(fishes: list[int]) -> list[int]:
    days = [0] * 9
    for fish in fishes:
        days[fish] += 1
    return days


def day_pass(days: list[int]) -> list[int]:
    # Move all fish to the left and store the left-most in variable
    left_most = days[0]
    days[0] = 0
    for i in range(1, len(days)):
        days[i - 1] = days[i]

    # Add left_most fish to day 6 and 8
    days[6] += left_most
    days[8] = left_most
    return days


if __name__ == '__main__':
    day6part2()
