from part1 import get_input, is_corrupted


def day10part2(filename: str) -> int:
    _input = get_input(filename)
    points = []
    for line in _input:
        corruption = is_corrupted(line)
        if not corruption[0]:
            total = 0
            for char in corruption[2]:
                total *= 5
                if char == ')':
                    total += 1
                elif char == ']':
                    total += 2
                elif char == '}':
                    total += 3
                elif char == '>':
                    total += 4
            points.append(total)

    sorted_points = sorted(points)
    middle_idx = len(sorted_points) // 2
    return sorted_points[middle_idx]


if __name__ == '__main__':
    print(day10part2('input.txt'))
