def day8part1(file_name: str) -> int:
    inputs = get_input(file_name)
    return count_easy(inputs)


def count_easy(lines: list[list[list[str]]]) -> int:
    counter = 0
    for line in lines:
        for nums in line[1]:
            if len(nums) == 2 or len(nums) == 3 or len(nums) == 4 or len(nums) == 7:
                counter += 1

    return counter


def get_input(file_name: str) -> list[list[list[str]]]:
    lines = []
    with open(file_name, "r") as f:
        lines += f.read().splitlines()
    lines = [x.split('|') for x in lines]
    lines = [[x.strip().split(' ') for x in line] for line in lines]
    return lines


if __name__ == "__main__":
    print(day8part1("input.txt"))
