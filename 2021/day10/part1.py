"""
Code duplication galore!
Once again, though, I win in the end, because - IT WORKS!
"""


def day10part1(filename: str) -> int:
    _input = get_input(filename)
    points = []
    for i in _input:
        corruption = is_corrupted(i)
        if corruption[0]:
            if corruption[1] == '}':
                points.append(1197)
            elif corruption[1] == ']':
                points.append(57)
            elif corruption[1] == ')':
                points.append(3)
            elif corruption[1] == '>':
                points.append(25137)
    return sum(points)


def get_input(filename: str) -> list[list[str]]:
    _input = []
    with open(filename) as f:
        _input = f.read().splitlines()
    _input = [list(x) for x in _input]
    return _input


def is_corrupted(inp: list[str]) -> (bool, str, list[str]):
    openings = 0
    closings = 0
    needs_to_close_with = []
    for i in inp:
        if i == '{':
            openings += 1
            needs_to_close_with.append('}')
        elif i == '[':
            openings += 1
            needs_to_close_with.append(']')
        elif i == '(':
            openings += 1
            needs_to_close_with.append(')')
        elif i == '<':
            openings += 1
            needs_to_close_with.append('>')
        elif i == '}':
            closings += 1
            if needs_to_close_with[-1] == i:
                needs_to_close_with.pop()
            else:
                return True, i, []
        elif i == ']':
            closings += 1
            if needs_to_close_with[-1] == i:
                needs_to_close_with.pop()
            else:
                return True, i, []
        elif i == ')':
            closings += 1
            if needs_to_close_with[-1] == i:
                needs_to_close_with.pop()
            else:
                return True, i, []
        elif i == '>':
            closings += 1
            if needs_to_close_with[-1] == i:
                needs_to_close_with.pop()
            else:
                return True, i, []

    return False, '', list(reversed(needs_to_close_with))


if __name__ == '__main__':
    print(day10part1('test.txt'))
