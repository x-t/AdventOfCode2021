"""
Warning: not for the faint of heart.
This one's particularly ugly.
It works, and I don't care, but this is about as ugly as it gets.

To understand *some* of the logic behind it, see logic.txt
But even then, it's pretty much a black box.
"""

from part1 import get_input


def day8part2(file_name: str) -> int:
    inputs = get_input(file_name)
    segments = []
    for _input in inputs:
        smap = mappy(_input[0])
        segment = []
        for nums in _input[1]:
            segment.append(num_out_of_segments(unscramble(nums, smap)))
        segments.append(int(''.join(map(str, segment))))
    return sum(segments)


def mappy(_input: list[str]) -> dict:
    smap = {}
    one, two, three, four, five, six, seven, eight, nine = '', '', '', '', '', '', '', '', ''
    for num in _input:
        if len(num) == 2:
            one = num
        elif len(num) == 3:
            seven = num
        elif len(num) == 4:
            four = num
        elif len(num) == 7:
            eight = num
    # Get the character that is in seven and not in one
    for char in seven:
        if char not in one:
            smap[char] = 'a'
    # Get all numbers that are 6 characters long
    six_long = []
    for num in _input:
        if len(num) == 6:
            six_long.append(num)
    # Get the number from six_long that does not
    # contain characters from one
    one_one, one_two = list(one)
    for sixes in six_long:
        if one_one not in sixes or one_two not in sixes:
            six = sixes
            if one_one not in sixes:
                smap[one_one] = 'c'
                smap[one_two] = 'f'
            if one_two not in sixes:
                smap[one_two] = 'c'
                smap[one_one] = 'f'
    six_long.remove(six)
    # Get the number from six_long that contains
    # all segments from four
    for sixes in six_long:
        if four[0] in sixes and four[1] in sixes and four[2] in sixes and four[3] in sixes:
            nine = sixes
    six_long.remove(nine)
    zero = six_long[0]
    # Find the segment present in four that's missing in zero
    for char in four:
        if char not in zero:
            smap[char] = 'd'
    # Remove known numbers from the list
    _input.remove(zero)
    _input.remove(one)  # Missing: 2, 3
    _input.remove(four)  # Missing: 5
    _input.remove(six)
    _input.remove(seven)
    _input.remove(eight)
    _input.remove(nine)
    # Find the number (3) that contains all letters from smap
    lets = list(smap.keys())
    for num in _input:
        if set(lets).issubset(set(num)):
            three = num
            # The letter lets doesn't contain and num does is G
            for char in num:
                if char not in lets:
                    smap[char] = 'g'
                    lets.append(char)
    _input.remove(three)
    # Get the unmapped letter from four, which is B
    for char in four:
        if char not in lets:
            smap[char] = 'b'
            lets.append(char)

    # Get the unmapped letter from eight, which is E
    for char in eight:
        if char not in lets:
            smap[char] = 'e'
            lets.append(char)

    return smap


# lol. i'm tired.
def num_out_of_segments(num: str) -> int:
    segments = list(num)
    zero = ['a', 'b', 'c', 'e', 'f', 'g']
    one = ['c', 'f']
    two = ['a', 'c', 'd', 'e', 'g']
    three = ['a', 'c', 'd', 'f', 'g']
    four = ['b', 'c', 'd', 'f']
    five = ['a', 'b', 'd', 'f', 'g']
    six = ['a', 'b', 'd', 'e', 'f', 'g']
    seven = ['a', 'c', 'f']
    eight = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nine = ['a', 'b', 'c', 'd', 'f', 'g']
    if set(segments) == set(zero):
        return 0
    elif set(segments) == set(one):
        return 1
    elif set(segments) == set(two):
        return 2
    elif set(segments) == set(three):
        return 3
    elif set(segments) == set(four):
        return 4
    elif set(segments) == set(five):
        return 5
    elif set(segments) == set(six):
        return 6
    elif set(segments) == set(seven):
        return 7
    elif set(segments) == set(eight):
        return 8
    elif set(segments) == set(nine):
        return 9


def unscramble(num: str, smap: dict) -> str:
    g = []
    for n in num:
        g.append(smap[n])
    return ''.join(g)


if __name__ == "__main__":
    print(day8part2("input.txt"))
