def day14part1(filename: str) -> int:
    thing, instructions = fix_input(filename)
    for _ in range(10):
        insertions = []
        for instruction in instructions:
            substr, substitute = instruction
            if substr in thing:
                for find in find_all_in_str(thing, substr):
                    insertions.append((find, substr, substitute))
        insertions = sorted(insertions, key=lambda x: x[0])
        for insertion in range(len(insertions)):
            thing = insert_char(thing, insertions[insertion][0] + insertion + 1, insertions[insertion][2])
    occurrences = count_occurrences(thing)
    occurrences_list = [occurrences[key] for key in occurrences]
    return max(occurrences_list) - min(occurrences_list)


def find_all_in_str(string: str, substring: str) -> list:
    indexes = []
    for char in range(len(string)):
        if string[char:char + len(substring)] == substring:
            indexes.append(char)
    return indexes


# Insert a character at a given index
def insert_char(thing: str, index: int, char: str) -> str:
    return thing[:index] + char + thing[index:]


# Count character occurrences
def count_occurrences(string: str) -> dict:
    return {char: string.count(char) for char in string}


def fix_input(filename: str) -> (str, list):
    def get_input(_filename: str) -> list:
        with open(_filename) as f:
            return [line.strip('\n') for line in f]

    _input = get_input(filename)
    thing = _input[0]
    _input = _input[2:]
    _input = [line.split(' -> ') for line in _input]

    return thing, _input


if __name__ == '__main__':
    print(day14part1('input.txt'))
