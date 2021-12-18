# Another day, another optimisation task...

import math

from part1 import fix_input


def day14part2(filename: str) -> int:
    thing, instructions = fix_input(filename)
    segs = split_segments(thing)
    for _ in range(40):
        to_remove = []
        to_add = []
        for instruction in instructions:
            segment, substitution = instruction
            if segment in segs:
                times_had = segs[segment]
                to_remove.append(segment)
                to_add.append((segment[0] + substitution, times_had))
                to_add.append((substitution + segment[1], times_had))
        for r in to_remove:
            segs.pop(r)
        for a in to_add:
            try:
                segs[a[0]] += a[1]
            except KeyError:
                segs[a[0]] = a[1]

    res = count_occurrences(segs)
    res_list = [res[key] for key in res]
    return max(res_list) - min(res_list)


def count_occurrences(segments: dict) -> dict:
    occurrences = {}
    for segment in segments.items():
        try:
            occurrences[segment[0][0]] += segment[1]
        except KeyError:
            occurrences[segment[0][0]] = segment[1]
        try:
            occurrences[segment[0][1]] += segment[1]
        except KeyError:
            occurrences[segment[0][1]] = segment[1]
    # I genuinely have no idea why they're all doubled lmao
    for k, v in occurrences.items():
        occurrences[k] = math.ceil(v / 2)
    return occurrences


def split_segments(string: str) -> dict:
    segments = {}
    for char in range(len(string)):
        seg = string[char:char + 2]
        if len(seg) == 2:
            try:
                segments[seg] += 1
            except KeyError:
                segments[seg] = 1
    return segments


if __name__ == '__main__':
    print(day14part2('input.txt'))
